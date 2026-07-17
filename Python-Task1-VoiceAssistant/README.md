#  Voice Assistant

###  Features

**Voice Recognition**: Captures user input using `speech_recognition` via your microphone.

**Natural Language Interaction**: Responds naturally with text-to-speech using `pyttsx3`.

**Web Search**: Automatically redirects queries to Google for broad information retrieval.

**Time & Date**: Provides accurate real-time updates upon request.

**Live Weather**: Fetches precise weather updates using the OpenWeatherMap API.

**General Knowledge**: Answers factual questions using the WolframAlpha Computational Knowledge Engine.

**Email Automation**: Effortlessly sends emails via voice command using `smtplib`.

**Timed Reminders**: Triggers audible alerts after a specified duration using multi-threading.

---

###  Additional Enhancements

**Voice Modulation**: Ability to switch between available voice profiles.

**Speech Speed Control**: Dynamically adjusts the assistant's speaking rate.

**Background Execution**: Uses `threading` to ensure the assistant remains responsive while timers or reminders are running.

---

###  Privacy & Data Processing

**Local Processing**: Audio input is processed locally by the speech recognition engine.

**Data Handling**: No user interaction data or personal information is stored on external servers or databases.

**Security**: API keys and email credentials are handled via environment variables (or local configuration) to ensure user privacy and code security.

---

###  Tech Stack

**Language**: Python 3.x

**Required Libraries**: `speech_recognition`, `pyttsx3`, `requests`, `wolframalpha`, `smtplib`

---

###  How to Run

1. **Clone the repository**:
`git clone https://github.com/your-username/voice-assistant.git`

2. **Install dependencies**:
`pip install -r requirements.txt`

3. **Configure API Keys**:
Set up your personal API keys for **OpenWeatherMap** and **WolframAlpha**.

4. **Launch the assistant**:
`python main.py`

---

<span style="font-size:18px">Developed by Lavanya Trivedi</span>
