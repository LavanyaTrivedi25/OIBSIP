import os
import sqlite3
from flask import Flask
from flask_socketio import SocketIO, join_room, leave_room, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chat_secret_key_123'
socketio = SocketIO(app, cors_allowed_origins="*")

DB_FILE = "chat_database.db"

def init_db():
    """Initializes SQLite database for users and message history."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    # Messages table for room history
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room TEXT NOT NULL,
            username TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@socketio.on('register')
def handle_register(data):
    username = data.get('username')
    password = data.get('password')
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        emit('auth_response', {'status': 'success', 'message': 'Registration successful!'})
    except sqlite3.IntegrityError:
        emit('auth_response', {'status': 'error', 'message': 'Username already exists.'})
    finally:
        conn.close()

@socketio.on('login')
def handle_login(data):
    username = data.get('username')
    password = data.get('password')
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        emit('auth_response', {'status': 'success', 'username': username})
    else:
        emit('auth_response', {'status': 'error', 'message': 'Invalid username or password.'})

@socketio.on('join_room')
def handle_join(data):
    room = data.get('room')
    username = data.get('username')
    join_room(room)
    
    # Load past messages from SQLite history
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT username, message, timestamp FROM messages WHERE room = ? ORDER BY id ASC", (room,))
    rows = cursor.fetchall()
    conn.close()
    
    history = [{'username': r[0], 'message': r[1], 'timestamp': r[2]} for r in rows]
    emit('load_history', {'history': history})
    
    emit('message', {'username': 'System', 'message': f'{username} has joined the room.', 'timestamp': ''}, room=room)

@socketio.on('send_message')
def handle_message(data):
    room = data.get('room')
    username = data.get('username')
    message = data.get('message')
    timestamp = data.get('timestamp')
    
    # Save message to SQLite history
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (room, username, message, timestamp) VALUES (?, ?, ?, ?)",
                   (room, username, message, timestamp))
    conn.commit()
    conn.close()
    
    emit('message', {'username': username, 'message': message, 'timestamp': timestamp}, room=room)

if __name__ == '__main__':
    init_db()
    print("[*] Starting Flask-SocketIO Chat Server on port 5000...")
    socketio.run(app, host='127.0.0.1', port=5000)