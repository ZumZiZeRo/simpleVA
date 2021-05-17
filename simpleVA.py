import pyttsx3
import speech_recognition as sr
import os
import threading


class Alfred():
    listOfCommands = [{
        'open steam': 'os.startfile(D:\Steam\steam.exe)'
    }]

    def __init__(self):
        self.voiceRecognition = sr.Recognizer()
        self.voice = pyttsx3.init()
        self.voice.setProperty('rate', 140)
        self.voice.startLoop()
        print('Alfred initialized')

    def AlfredVoice(self, msg):
        self.voice.say(msg)

    def callForAlfred(self):
        self.AlfredVoice('alfred is at your service, master.')
        self.voice.iterate()
        while True:
            with sr.Microphone() as source:
                print('call alfred')
                call = self.voiceRecognition.listen(source)
                callInput = self.voiceRecognition.recognize_google(
                    call).lower()
                if 'alfred' in callInput:
                    command = self.listenForCommands()
                    self.runCommands(command)
                else:
                    self.AlfredVoice('are you talking to me?')
                    self.voice.iterate()

    def listenForCommands(self):
        self.AlfredVoice('Yes, Master!')
        self.voice.iterate()
        with sr.Microphone() as source:
            print('Give your Command')
            commandInput = self.voiceRecognition.listen(source)
            print(self.voiceRecognition.recognize_google(commandInput))
            return self.voiceRecognition.recognize_google(commandInput)

    def runCommands(self, command):
        for item in self.listOfCommands:
            if command.lower() in item.keys():
                self.AlfredVoice('as you wish sir.')
                self.voice.iterate()
                self.voice.endLoop()
                exec(item[command.lower])


alfredVA = Alfred()
listen = threading.Thread(target=alfredVA.callForAlfred, args=())
listen.start()

# def speech_to_text():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         audio = r.listen(source)
#         print(r.recognize_google(audio))
#         if 'alfred' in r.recognize_google(audio).lower():
#             print('I heard you')

# speech_to_text()
