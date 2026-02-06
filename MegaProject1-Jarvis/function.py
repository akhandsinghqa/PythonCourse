import webbrowser

import pyttsx3
import requests

from ai_client import gemini_ai
from musiclib import music

engine = pyttsx3.init()
news_apikey = ""
engine.setProperty('rate', 150)


def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()


def play_music(command_song):
    print("Playing the song....")
    song = command_song.replace("play ", "").strip()
    if song in music:
        webbrowser.open(music[song])
    print(f"Playing {song}...")


def read_news():
    print("Reading the news......")
    try:
        res = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_apikey}")
        data = res.json()
        articles = data.get("articles", [])
        for i, article in enumerate(articles[:5]):
            speak(article["title"])
    except Exception as e:
        speak("I'm having trouble accessing the news right now.")


def ask_gemini(command_ask):
    gemini_response = gemini_ai(command_ask)
    print(gemini_response)
    speak(gemini_response)


def process_command(command):
    command = command.lower()
    print(" The command is : ", command)
    if "open gmail" in command:
        print("Opening the Gmail.....")
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    elif "open youtube" in command:
        print("Opening the Youtube.....")
        webbrowser.open("https://www.youtube.com/")
    elif command.startswith("play"):
        play_music(command)
    elif "news" in command:
        read_news()
    else:
        ask_gemini(command)
