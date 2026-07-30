**AI Personal Assistant (ITER Student Project)**
This project is a Python-based voice-controlled personal assistant designed to manage daily tasks, provide information, and improve productivity through automation.

**Features**
*Core Tasks*
Voice Recognition: Captures user input using speech_recognition via microphone.

Natural Language Interaction: Responds with text-to-speech using pyttsx3.

Web Search: Redirects queries to Google for broad information retrieval.

Time & Date: Provides real-time updates upon request.

Live Weather: Fetches weather updates using the OpenWeatherMap API.

General Knowledge: Answers factual questions using the WolframAlpha Computational Knowledge Engine.

Email Automation: Sends emails via voice command using smtplib.

Timed Reminders: Triggers audible alerts after a specified duration using multi-threading.

**Additional Enhancements**
Voice Modulation: Ability to switch between available voice profiles.

Speech Speed Control: Dynamically adjusts the assistant's speaking rate.

Background Execution: Uses threading to ensure the assistant remains responsive while timers or reminders are running.

**Privacy & Data Processing**
Local Processing: Audio input is processed locally by the speech_recognition engine.

Data Handling: No user interaction data or personal information is stored on external servers or databases.

Security: API keys and email credentials are handled via environment variables (or local configuration) to ensure user privacy and code security.

**Requirements**
Python 3.x

Required libraries: speech_recognition, pyttsx3, requests, wolframalpha, smtplib.

**How to Run**
Clone the repository.

Install dependencies: pip install -r requirements.txt (or install manually).

Set up your API keys for OpenWeatherMap and WolframAlpha.

Run the main script: python main.py