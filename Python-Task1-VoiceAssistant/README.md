# Python Voice Assistant (Task 1)

A command-line voice assistant built in Python that utilizes speech recognition, text-to-speech synthesis, APIs, and local device capabilities to execute common voice commands, fetch real-time information, and manage basic productivity tasks.

---

## Tech Stack
- **Language**: Python 3.x
- **Speech Processing**: `speech_recognition`, `pyttsx3`
- **APIs & Web**: `requests`, `webbrowser`, `wolframalpha`
- **Utilities**: `smtplib` (Email), `threading`, `winsound`

---

## Key Features
- **Speech-to-Text & Text-to-Speech**: Listens to microphone audio inputs and responds via synthesized speech and terminal logs.
- **Real-Time Weather Integration**: Fetches current temperature and descriptions for specified cities using the OpenWeatherMap API.
- **General Knowledge & Computation**: Retrieves answers and performs calculations using the WolframAlpha API.
- **Automated Email Dispatch**: Sends emails via SMTP using Gmail credentials and a local contacts mapping.
- **Background Reminders**: Sets timed reminders using multithreading and triggers audible alerts with `winsound`.
- **Web Search Fallback**: Automatically opens default web searches via `webbrowser` if a query does not match a specific built-in intent.

---

## 🚀 Setup & Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/LavanyaTrivedi25/OIBSIP.git
cd Python-Task1-VoiceAssistant
