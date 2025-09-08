Voice-Controlled Assistant

#Overview

This project is a simple voice-controlled assistant implemented in Python. It listens to user voice commands through the microphone, processes them using speech recognition, and performs a variety of predefined actions such as opening applications, launching websites, providing the current time, or giving information about the project. The assistant responds verbally using text-to-speech synthesis, allowing hands-free interaction.

##Features

Voice input via microphone using speech_recognition

Voice output using pyttsx3 text-to-speech engine



##commands implemented include:

Greeting and assistance ("hello")

Opening Notepad application

Opening Google and LinkedIn websites

Searching for Python developer jobs on LinkedIn

Reporting the current time

Providing information about the project

Exit command to stop the assistant



##Tools & Libraries:

Python 3.x

speech_recognition – for speech-to-text conversion

pyttsx3 – for text-to-speech output

os – to execute system commands

webbrowser – to open web pages

datetime – to provide current time information




##Supported Commands

"hello" – Greet and get assistance prompt

"open notepad" – Opens the Notepad application

"google" – Opens Google website

"open linkedin" – Opens LinkedIn website

"python developer jobs" – Opens LinkedIn job search for Python developers

"about the project" – Gives a brief description of the project

"time" – Speaks the current time

"exit", "quit", "stop" – Closes the assistant
