import speech_recognition as sr
import pyttsx3 as pt
import datetime
import webbrowser
import requests
import smtplib
import threading
import winsound
import wolframalpha  
import time

API_KEY = "8ff80a92ba47e122b45dac4ad7962d3a"
WOLFRAM_APP_ID = "6KH36XY9QG"  
MY_EMAIL = "lavanyatrivedi25@gmail.com"
MY_PASSWORD = "cmpq avey gpiy aful"

wolfram_client = wolframalpha.Client(WOLFRAM_APP_ID)

engine = pt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

def speak(text):
    print(f"Assistant: {text}")
    try:
        time.sleep(1)
        engine.say(text)
        engine.runAndWait()
    except RuntimeError:
        pass

def listen():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now. I am Listening...")
        rec.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = rec.listen(source, timeout=30, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            return "none"
    try:
        query = rec.recognize_google(audio, language='en-in')
        return query.lower()
    except:
        return "none"

def get_qa_answer(query):
    try:
        res = wolfram_client.query(query)
        ans = next(res.results).text
        return ans
    except:
        return "I couldn't find an answer in my knowledge base."

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},IN&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url).json()
        if response.get("cod") == "200":
            temp = response["list"][0]["main"]["temp"]
            desc = response["list"][0]["weather"][0]["description"]
            return f"Currently in {city}, it is {desc} at {temp} degrees."
        return "Unable to fetch weather."
    except:
        return "Weather service unreachable."

def send_email(to, subject, content, sender_name):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(MY_EMAIL, MY_PASSWORD)
    server.sendmail(MY_EMAIL, to, f"Subject: {subject}\n\n{content}\n\nRegards, {sender_name}")
    server.close()

def set_reminder(seconds, message):
    def reminder_thread():
        time.sleep(seconds)
        speak(f"Reminder: {message}")
        winsound.Beep(1000, 2000)
    threading.Thread(target=reminder_thread).start()

def main():
    global current_voice_index, current_rate
    speak("Hello! I am your personal assistant.")
    speak("You can ask me about the time, weather, general knowledge, set reminders, or even send emails.")
    
    while True:
        query = listen()
        if query == "none": continue

        if 'time' in query:
            speak(f"The time is {datetime.datetime.now().strftime('%I:%M %p')}")
        
        elif 'weather' in query:
            speak("Which city?")
            city = listen()
            if city != "none": speak(get_weather(city))
            
        elif 'what is' in query or 'who is' in query or 'calculate' in query:
            speak("Searching my knowledge base...")
            speak(get_qa_answer(query))
        
        # Ensure this block is in your main logic chain
        elif 'send email' in query or 'email' in query:
            try:
                speak("What should be the subject?")
                subject = listen()
                speak("What should I say?")
                content = listen()
                speak("To whom should I send this?")
                recipient = listen()
                
                # Yahan recipient ke hisaab se email ID mapping ka use karein
                # Jaise: target_email = contacts[recipient]
                
                send_email(target_email, subject, content, "Assistant")
                speak("Email has been sent successfully.")
            except Exception as e:
                speak("I am sorry, I was unable to send the email.")

        elif 'reminder' in query:
            speak("What should I remind you about?")
            msg = listen()
            speak("After how much time in minutes?")
            mins = listen()
            try:
                val = int(''.join(filter(str.isdigit, mins)))
                set_reminder(val * 60, msg)
                speak(f"Reminder set for {val} minutes.")
            except: speak("Invalid time format.")

        elif 'exit' in query or 'stop' in query:
            speak("Okay, Bye! See you next time.")
            break
        else:
            speak("Searching on Google.")
            webbrowser.open(f"https://www.google.com/search?q={query}")

if __name__ == "__main__":
    main()