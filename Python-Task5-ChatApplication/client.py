import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime
import socketio

sio = socketio.Client()

emojis = {
    ":smile:": "😊",
    ":laugh:": "😂",
    ":heart:": "❤️",
    ":thumbsup:": "👍",
    ":fire:": "🔥",
    ":sad:": "😢",
    ":wink:": "😉",
    ":sunglasses:": "😎"
    }

def replace_emoji(text):
    for code, emoji in emojis.items():
        text = text.replace(code, emoji)
    return text

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Application")
        self.root.geometry("650x550")
        self.root.resizable(False, False)
        self.current_user = None
        self.current_room = None
        
        self.is_focused = True
        self.root.bind("<FocusIn>", self.on_focus_in)
        self.root.bind("<FocusOut>", self.on_focus_out)
        
        self.setup_socket_events()
        self.create_auth_screen()

    def on_focus_in(self, event):
        self.is_focused = True
        self.root.title("Chat Application")

    def on_focus_out(self, event):
        self.is_focused = False

    def setup_socket_events(self):
        @sio.on('auth_response')
        def on_auth(data):
            if data.get('status') == 'success':
                if 'username' in data:
                    self.current_user = data['username']
                    self.show_room_screen()
                else:
                    messagebox.showinfo("Success", data.get('message'))
            else:
                messagebox.showerror("Error", data.get('message'))

        @sio.on('load_history')
        def on_history(data):
            self.chat_display.config(state=tk.NORMAL)
            self.chat_display.delete('1.0', tk.END)
            for item in data.get('history', []):
                prefix = f"[{item['timestamp']}] " if item['timestamp'] else ""
                formatted = f"{prefix}{item['username']}: {item['message']}\n"
                self.chat_display.insert(tk.END, formatted)
            self.chat_display.config(state=tk.DISABLED)
            self.chat_display.see(tk.END)

        @sio.on('message')
        def on_message(data):
            prefix = f"[{data['timestamp']}] " if data['timestamp'] else ""
            msg = replace_emoji(data['message'])
            format = f"{prefix}{data['username']}: {msg}\n"
            
            self.chat_display.config(state=tk.NORMAL)
            self.chat_display.insert(tk.END, format)
            self.chat_display.config(state=tk.DISABLED)
            self.chat_display.see(tk.END)
            
            if not self.is_focused and data['username'] != self.current_user:
                self.root.title(f"(*) New Message in {self.current_room}!")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_auth_screen(self):
        self.clear_window()
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="Chat Login / Register", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(frame, text="Username:", font=("Arial", 10)).pack(anchor="w")
        self.username_entry = tk.Entry(frame, font=("Arial", 11), width=25)
        self.username_entry.pack(pady=5)

        tk.Label(frame, text="Password:", font=("Arial", 10)).pack(anchor="w")
        self.password_entry = tk.Entry(frame, font=("Arial", 11), width=25, show="*")
        self.password_entry.pack(pady=5)

        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="Login", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=10, command=self.handle_login).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Register", bg="#2196F3", fg="white", font=("Arial", 10, "bold"), width=10, command=self.handle_register).pack(side=tk.LEFT, padx=5)

    def handle_login(self):
        userid = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        if not userid or not password:
            messagebox.showwarning("Warning", "Please enter both username and password.")
            return
        try:
            if not sio.connected:
                sio.connect('http://127.0.0.1:5000')
            sio.emit('login', {'username': userid, 'password': password})
        except Exception as e:
            messagebox.showerror("Connection Error", f"Could not connect to server: {e}")

    def handle_register(self):
        userid = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        if not userid or not password:
            messagebox.showwarning("Warning", "Please enter both username and password.")
            return
        try:
            if not sio.connected:
                sio.connect('http://127.0.0.1:5000')
            sio.emit('register', {'username': userid, 'password': password})
        except Exception as e:
            messagebox.showerror("Connection Error", f"Could not connect to server: {e}")

    def show_room_screen(self):
        self.clear_window()
        
        top_frame = tk.Frame(self.root, pady=10, padx=10)
        top_frame.pack(fill="x")

        tk.Label(top_frame, text=f"Logged in as: {self.current_user}", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        
        tk.Label(top_frame, text="Room:", font=("Arial", 10)).pack(side=tk.LEFT, padx=(20, 5))
        self.room_entry = tk.Entry(top_frame, font=("Arial", 10), width=15)
        self.room_entry.pack(side=tk.LEFT, padx=5)
        self.room_entry.insert(0, "General")

        tk.Button(top_frame, text="Join Room", bg="#FF9800", fg="white", font=("Arial", 9, "bold"), command=self.join_chat_room).pack(side=tk.LEFT, padx=5)

        # Chat display 
        chat_frame = tk.Frame(self.root, padx=10)
        chat_frame.pack(fill="both", expand=True)

        self.chat_display = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, font=("Arial", 10), state=tk.DISABLED)
        self.chat_display.pack(fill="both", expand=True, pady=5)

        # Bottom entry 
        bottom_frame = tk.Frame(self.root, pady=10, padx=10)
        bottom_frame.pack(fill="x")

        self.msg_entry = tk.Entry(bottom_frame, font=("Arial", 11))
        self.msg_entry.pack(side=tk.LEFT, fill="x", expand=True, padx=(0, 5))
        self.msg_entry.bind("<Return>", lambda event: self.send_message())

        tk.Button(bottom_frame, text="Send", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=10, command=self.send_message).pack(side=tk.RIGHT)

        # to auto join the default created room
        self.join_chat_room()

    def join_chat_room(self):
        room = self.room_entry.get().strip()
        if not room:
            messagebox.showwarning("Warning", "Room name cannot be empty.")
            return
        self.current_room = room
        sio.emit('join_room', {'room': room, 'username': self.current_user})

    def send_message(self):
        msg = self.msg_entry.get().strip()
        if not msg:
            return
        timestamp = datetime.now().strftime('%H:%M')
        sio.emit('send_message', {
            'room': self.current_room,
            'username': self.current_user,
            'message': msg,
            'timestamp': timestamp
        })
        self.msg_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.onscreen = lambda: None
    root.mainloop()