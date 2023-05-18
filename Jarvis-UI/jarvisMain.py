import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import pywhatkit
from pyautogui import moveTo, write, leftClick
import pyjokes
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from jarvisMainGui import Ui_JarvisMainGUI
import openai

api_data = "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"
openai.api_key = api_data
completion = openai.Completion()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)
engine.setProperty('volume', 2.0)


def Reply(question):
    prompt = f'Iman: {question}\n Jarvis: '
    response = completion.create(
        model="text-davinci-003",
        prompt="",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    answer = response.choices[0].text.strip()
    return answer


def speak(audio):
    ui.updatedMovieDinamically("speaking")
    engine.say(audio)
    engine.runAndWait()


def wishings():
    ui.updatedMovieDinamically("speaking")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        ui.terminalPrint('Good morning BOSS')
        speak('Good morning BOSS')
    elif hour >= 12 and hour < 17:
        ui.terminalPrint("Good Afternoon BOSS")
        speak("Good Afternoon BOSS")
    elif hour >= 17 and hour < 21:
        ui.terminalPrint("Good Evening BOSS")
        speak("Good Evening BOSS")
    else:
        ui.terminalPrint("Good Night BOSS")
        speak("Good Night BOSS")


class jarvisMainClass(QThread):
    def __init__(self):
        super(jarvisMainClass, self).__init__()

    def run(self):
        self.runJarvis()

    def commands(self):
        ui.updatedMovieDinamically("listening")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            ui.terminalPrint("[LISTENING...]")
            r.pause_threshold = 3
            r.energy_threshold = 300
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, 0, 7)

        try:
            ui.updatedMovieDinamically("loading")
            ui.terminalPrint("[RECOGNIZING...]")
            query = r.recognize_google(audio, language='en-in', show_all=True)
            alternative = query['alternative'][0]['transcript']
            confidence = query['alternative'][0]['confidence']
            ui.terminalPrint(f"Your Command :  {alternative}\n")
            ui.terminalPrint(f"Confidence : {confidence}\n")
        except:
            return "None"

        return alternative.lower()

    def there_exists(self, terms):
        for term in terms:
            if term in self.query:
                return True

    def searchGoogle(self, query):
        if "google search" in self.query:
            import wikipedia as googleScrap
            self.query = self.query.replace("jarvis", "")
            self.query = self.query.replace("google search", "")
            self.query = self.query.replace("google", "")
            speak("This is what I found on google")

            try:
                pywhatkit.search(self.query)
                result = googleScrap.summary(self.query, 1)
                speak(result)

            except:
                speak("No speakable output available")

    def searchYoutube(query):
        if "youtube" in query:
            speak("This is what I found for your search!")
            query = query.replace("youtube search", "")
            query = query.replace("youtube", "")
            query = query.replace("jarvis", "")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            pywhatkit.playonyt(query)
            speak("Done, Sir")

    def searchWikipedia(query):
        if "wikipedia" in query:
            speak("Searching from wikipedia....")
            query = query.replace("wikipedia", "")
            query = query.replace("search wikipedia", "")
            query = query.replace("jarvis", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to wikipedia..")
            print(results)
            speak(results)

    def runJarvis(self):
        wishings()
        while True:
            self.query = self.commands().lower()
            if 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak("Sir, The time is: " + strTime)
                ui.terminalPrint(strTime)

            elif self.there_exists(['hello', 'hi']):
                ui.terminalPrint("Hello bos")
                speak("hello bos")
            elif self.there_exists(['iam fine', 'i am fine']):
                speak("that's great, sir")
            elif "how are you" in self.query:
                speak("Perfect, sir")
            elif "thank you" in self.query:
                speak("you are welcome, sir")
            elif "google search" in self.query:
                self.searchGoogle(self.query)
            elif 'wikipedia' in self.query:
                speak("Searching in wikipedia")
                try:
                    self.query = self.query.replace("wikipedia", '')
                    results = wikipedia.summary(self.query, sentences=1)
                    speak("According to Wikipedia..")
                    ui.terminalPrint(results)
                    speak(results)
                except:
                    ui.terminalPrint("No results found..")
                    speak("no results found")

            elif 'play' in self.query:
                playquery = self.query.replace('play', '')
                speak("Playing " + playquery)
                pywhatkit.playonyt(playquery)

            elif 'type' in self.query:
                speak("Please tell me what should i write")
                while True:
                    typequery = self.commands()
                    if typequery == "exit typing":
                        speak("Done Sir")
                        break
                    else:
                        write(typequery)

            elif 'minimize' in self.query or 'minimise' in self.query:
                moveTo(1232, 15)
                leftClick()

            elif 'joke' in self.query:
                jarvisJoke = pyjokes.get_joke()
                ui.terminalPrint(jarvisJoke)
                speak(jarvisJoke)

            else:
                ans = Reply(self.query)
                ui.terminalPrint(ans)
                speak(ans)


startExecution = jarvisMainClass()


class Ui_Jarvis(QMainWindow):
    def __init__(self):
        super(Ui_Jarvis, self).__init__()
        self.jarvisUI = Ui_JarvisMainGUI()
        self.jarvisUI.setupUi(self)

        self.jarvisUI.exitButton.clicked.connect(self.close)
        self.jarvisUI.enterButton.clicked.connect(self.manualCodeFromTerminal)

        self.runAllMovies()

    def manualCodeFromTerminal(self):
        if self.jarvisUI.terminalInputBox.text():
            cmd = self.jarvisUI.terminalInputBox.text()
            self.jarvisUI.terminalInputBox.clear()
            self.jarvisUI.terminalOutputBox.appendPlainText(
                f"You Typed -> {cmd}")

            if cmd == 'exit':
                ui.close()
            elif cmd == 'help':
                self.terminalPrint(
                    "I can realize what your answer sir, anything")

            else:
                pass

    def terminalPrint(self, text):
        self.jarvisUI.terminalOutputBox.appendPlainText(text)

    def updatedMovieDinamically(self, state):
        if state == "speaking":
            self.jarvisUI.jarvisSpeakingLabel.raise_()
            self.jarvisUI.jarvisSpeakingLabel.show()
            self.jarvisUI.listeningLabel.hide()
            self.jarvisUI.loadingLabel.hide()
        elif state == "listening":
            self.jarvisUI.listeningLabel.raise_()
            self.jarvisUI.listeningLabel.show()
            self.jarvisUI.jarvisSpeakingLabel.hide()
            self.jarvisUI.loadingLabel.hide()
        elif state == "loading":
            self.jarvisUI.loadingLabel.raise_()
            self.jarvisUI.loadingLabel.show()
            self.jarvisUI.jarvisSpeakingLabel.hide()
            self.jarvisUI.listeningLabel.hide()

    def runAllMovies(self):
        # Jarvis GUI
        self.jarvisUI.codingMovie = QtGui.QMovie(
            "D:\\python programs\\TUGAS AKHIR\\GUI files-20230328T090529Z-001\\GUI files\\B.G_Template_1.gif")
        self.jarvisUI.codingLabel.setMovie(self.jarvisUI.codingMovie)
        self.jarvisUI.codingMovie.start()
        # ironManBackground
        self.jarvisUI.listeningMovie = QtGui.QMovie(
            "D:\\python programs\\TUGAS AKHIR\\GUI files-20230328T090529Z-001\\GUI files\\listening.gif")
        self.jarvisUI.listeningLabel.setMovie(self.jarvisUI.listeningMovie)
        self.jarvisUI.listeningMovie.start()
        # ironmanGIF
        self.jarvisUI.speakingMovie = QtGui.QMovie(
            "D:\\python programs\\TUGAS AKHIR\\GUI files-20230328T090529Z-001\\GUI files\\speaking.gif")
        self.jarvisUI.jarvisSpeakingLabel.setMovie(self.jarvisUI.speakingMovie)
        self.jarvisUI.speakingMovie.start()
        # dateLabel
        self.jarvisUI.arcMovie = QtGui.QMovie(
            "D:\\python programs\\TUGAS AKHIR\\GUI files-20230328T090529Z-001\\GUI files\\techcircle.gif")
        self.jarvisUI.arcLabel.setMovie(self.jarvisUI.arcMovie)
        self.jarvisUI.arcMovie.start()
        # timeLabel
        self.jarvisUI.loadingMovie = QtGui.QMovie(
            "D:\\python programs\\TUGAS AKHIR\\GUI files-20230328T090529Z-001\\GUI files\\tech loading-cropped.gif")
        self.jarvisUI.loadingLabel.setMovie(self.jarvisUI.loadingMovie)
        self.jarvisUI.loadingMovie.start()
        # startLabelNotButton

        startExecution.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_Jarvis()
    ui.show()
    sys.exit(app.exec_())
