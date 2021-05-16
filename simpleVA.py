import pyttsx3
import speech_recognition as sr
import os


def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something')
        _ = r.listen(source)
        print(r.recognize_google(_))
        return r.recognize_google(_)


ttsValue = speech_to_text()

voice = pyttsx3.init()  # ! rate:200,
voice.setProperty('rate', 120)
voice.say(ttsValue)
voice.runAndWait()
# os.startfile('D:/Steam/steam.exe')
