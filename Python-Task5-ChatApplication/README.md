# Chat Application (Task 5)

A full-stack, real-time desktop chat application featuring user authentication, multi-room chat support, persistent message history using SQLite, text-to-emoji shortcuts, and live notifications. The architecture is split into a Flask-SocketIO backend server and a `tkinter`-based desktop client.

---

## Tech Stack
- **Backend**: Python, `Flask`, `Flask-SocketIO`, `SQLite3`
- **Frontend / Client**: Python `tkinter`, `socketio.Client` (Python Socket.IO client library)
- **Utilities**: `datetime` for time-stamping messages

---

## Key Features
- **User Authentication**: Secure registration and login system with SQLite database storage.
- **Real-Time Communication**: Instant messaging powered by WebSockets via Flask-SocketIO.
- **Room Management**: Dynamic room-switching and joining capabilities allowing separate chat channels (defaulting to "General").
- **Message Persistence**: SQLite database stores historical chat messages per room, automatically loading past chats upon joining.
- **Emoji Shortcuts**: Text shortcuts (e.g., `:smile:`, `:heart:`, `:fire:`) automatically convert into corresponding emojis (`😊`, `❤️`, `🔥`).
- **Focus Detection & Notifications**: Detects when the application window is minimized or out of focus and updates the title bar dynamically with a notification indicator when a new message arrives.

---

## Setup & Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/LavanyaTrivedi25/OIRSIP.git
   cd Python-Task5-ChatApplication
