import speech_recognition as sr
import pyttsx3
import os, webbrowser, datetime

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Added ambient noise adjustment
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)  # timeout added
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I could not understand")
            return ""
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return ""
        except Exception as e:
            print("Error:", e)
            speak("Sorry, there was an error.")
            return ""

while True:
    cmd = take_command()
    if cmd == "":
        continue  # Skip empty commands caused by noise or recognition failure

    elif "hello" in cmd:
        print("Responding to 'hello' command")
        speak("Hello, I am your voice assistant. How can I help you today? Feel free to ask me anything.")

    elif "open notepad" in cmd:
        os.system("notepad")
        speak("Opening notepad")

    elif "google" in cmd:
        webbrowser.open("https://www.google.com")
        speak("Opening google")

    elif "open linkedin" in cmd:
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn")

    elif "python developer jobs" in cmd:
        webbrowser.open("https://www.linkedin.com/jobs/search/?keywords=python%20developer")
        speak("Here are some current Python developer jobs on LinkedIn")

    elif "about the project" in cmd:
        print("Responding to 'about the project' command")
        speak("This is a Voice Controlled Assistant project created using Python. "
          "It uses speech recognition for voice input and pyttsx3 for speech output. "
          "It can open applications, fetch information, and perform commands.")
        
    elif "time" in cmd:
        speak(datetime.datetime.now().strftime("%H:%M:%S"))
    
    elif "exit" in cmd or "quit" in cmd or "stop" in cmd:
        speak("Goodbye! Have a nice day.")
        break
    else:
        speak("Sorry, I don't have a command for that yet.")
 