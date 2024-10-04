import os
import time
import playsound3
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound3.playsound(filename)

speak("hello everyone, keep following me for more updates on my projects")
