import wolframalpha
import pyttsx3
import tkinter as tk
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
app_id = "K4KVKA-G225EG6WAH"  # Replace with your actual Wolfram Alpha API ID
client = wolframalpha.Client(app_id)
# GUI elements
root = tk.Tk()
root.title("AI Assistant")
root.geometry("400x400")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

output = tk.Text(root, height=20, width=50)
output.pack(pady=10)
def query_ai():
    user_input = entry.get()
    response = process_user_query(user_input)  # Replace with your actual logic
    output.insert(tk.END, "You: " + user_input + "\n")
    output.insert(tk.END, "AI: " + response + "\n\n")
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(response)
    engine.runAndWait()
def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    assname = ("Veronica 1.0")
    speak("I am your Assistant")
    speak(assname)


def username():
    speak("What should I call you sir?")
    uname = takeCommand()
    speak("Welcome Sir")
    speak(uname)

    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Sir.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can I Help you, Sir?")
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail
    server.login('your_email_id', 'your_email_password')
    server.sendmail('your_email_id', to, content)
    server.close()


# Main program loop
if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # Clear any command before execution
    clear()
    wishMe()
    username()

    while True:
        query = takeCommand().lower()

        # Execute functionalities based on user input
        # ... (your existing logic here) ... (call process_user_query)
        if query == "quit":
            break

        # Button to trigger AI interaction
        button = tk.Button(root, text="Send", command=query_ai)
