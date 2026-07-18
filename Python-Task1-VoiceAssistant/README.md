### Personal Voice Assistant

### Features 

**Voice Recognition: This voice assistant listens to you through your computer mic. It does so using something called `speech_recognition`. The voice assistant hears what you say. Then it does something with that information.

Natural Language Interaction The voice assistant replies to you in a human-like way. It uses `pyttsx3` to convert text into speech. The voice assistant says things to you. You can hear it.

Web Search: If you ask the voice assistant something it does not know it will search for the answer on Google. The voice assistant looks for answers on the internet.

Live Weather: The voice assistant will tell you the weather. It is fetching this information from the OpenWeatherMap API. The voice assistant knows what the weather is like.

General Knowledge: The voice assistant will answer the questions about lots of things. It uses the WolframAlpha Computational Knowledge Engine to find the answers to your queries.

Email Automation: You can ask the voice assistant to send an email. It will do this using `smtplib`. The voice assistant can send emails for you to an specific emails with personalised body.

Timed Reminders: The voice assistant can remind you of things. You can set a timer. It will alert you when the time is up and mention the work you were supposed to do.

---

### Additional Feature

Background Execution: The voice assistant can do things in the background. This means it can remind you of things or search for answers without stopping what it is doing. The voice assistant can do things at the same time.

---

### Privacy & Data Processing

Local Processing: The voice assistant listens to what you say on your computer. It strictly does not send what you say to anyone. The voice assistant keeps your conversations private and discrete.

Data Handling: The voice assistant does not keep any information about what you do. It does not store anything on any databases or servers. The voice assistant does not remember what you do.

Security: The voice assistant keeps your information safe. It uses something called environment variables in order to protect your API keys and email passwords. The voice assistant is very secure.

---

### Tech Stack

Language: The voice assistant is made using Python 3.12.4.

Required Libraries: The voice assistant needs libraries like `speech_recognition` `pyttsx3` `requests` `wolframalpha` and `smtplib` to work. These libraries help the voice assistant do things as described above.

---

### How to Run

1. Clone the repository: You can access the voice assistant's code from GitHub using `git clone https://github.com/your-username/voice-assistant.git`. This is the step to get the voice assistant.

2. Install dependencies: You need to install some libraries for the voice assistant to work. You can do this using `pip install -r requirements.txt`. This installation needs to be done in your command prompt or terminal, depending your your OS.

3. Configure API Keys: You'll need to set up your API keys for both OpenWeatherMap and WolframAlpha. You can have this by signing in to the websites and adding the API keys.

4. Run the assistant: You can run the voice assistant by running `python main.py` . This activates the voice assistant in your terminal.

---

<span style="font-size:19px">By Lavanya Trivedi</span>
