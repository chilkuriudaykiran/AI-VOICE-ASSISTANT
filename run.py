from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import re
import wikipedia
flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good night")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis At Your Service!")
        r.pause_threshold = 2
        command = r.listen(source)
    try:
        print("Recognizing...")
        recognized = r.recognize_google(command, language='en-in')
        print(recognized)
    except Exception as e:
        print(e)
        statement="Pardon sir.., I Couldn't Recognize Your Voice, If its nothing to command, i'll take a leave"
        print(statement)
        speak(statement)
        return None
    return recognized

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.JARVIS()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text

    def JARVIS(self):
        wish()
        while True:
            self.query = self.STT()
            if 'good bye' in self.query:
                sys.exit()
            elif 'open google' in self.query:
                webbrowser.open('www.google.co.in')
                speak("opening google")
            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
            elif 'play music' in self.query:
                speak("playing music from pc")
                self.music_dir ="./music"
                self.musics = os.listdir(self.music_dir)
                os.startfile(os.path.join(self.music_dir,self.musics[0]))
            elif 'notepad' in self.query:
                os.startfile("C:\\Windows\\notepad.exe")
            elif 'notepad' in self.query:
                os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.exe")
            elif "open chrome" in self.query:
                os.startfile("C:\\Windows\\notepad.exe")
            elif 'wikipedia' in self.query:  #if wikipedia found in the query then this block will be executed
                speak('Searching Wikipedia...')
                print('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "sachin tendulkar")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print("According to Wikipedia")
                print(results)
                speak(results)
            elif re.search("jokes|joke|Jokes|Joke", self.query):
                joke_ = obj.tell_me_joke('en', 'neutral')
                print(joke_)
                speak(joke_)
            elif re.search('weather|temperature', self.query):
                    # city = res.split(' ')[-1]
                    # weather_res = obj.weather(city=city)
                weather_res = obj.get_weather(self.query)
                print(weather_res)
                speak(weather_res)
            elif re.search('news', self.query):
                news_res = obj.news()
                pprint.pprint(news_res)
                speak(f"I have found {len(news_res)} news. You can read it. Let me tell you first 2 of them")
                speak(news_res[0])
                speak(news_res[1])
            elif re.search('date', self.query):
                date = obj.tell_me_date()
                print(date)
                print(speak(date))
            elif re.search('time', self.query):
                time = obj.tell_me_time()
                print(time)
                speak(time)
            elif "what is your name" in self.query:
                speak("iam jarvis ai voice assistant")
                print("iam jarvis ai voice assistant")
            elif 'how are you' in self.query:
                speak("I am fine, Thank you")
                print("I am fine, Thank you")
                speak("How are you, sir")
                print("How are you, sir")
            elif 'fine' in self.query or "good" in self.query:
                speak("It's good to know that your fine")
                print("It's good to know that your fine")
            elif "who are you" in self.query:
                speak("I am your jarvis voice assistant ")
                print("I am your jarvis voice assistant ")
            elif "open facebook" in self.query:
                webbrowser.open_new_tab("facebook.com")
            elif "make a note" in self.query:
                speak("What Should i write down sir?")
                print("What Should i write down sir?")
                note = takeCommand()
                remember = open('pytext.txt', 'w')
                remember.write(note)
                remember.close()
                speak("content added successfully in pytext.txt" + note)
                print("content added successfully in pytext.txt" + note)
            elif 'exit' in self.query:
                speak('sir . Call Me Anytime, at your service')
                print('sir . Call Me Anytime, at your service')
                quit()


def greet():
    t_hour = datetime.datetime.now().hour
    if 24> t_hour <4:
        speak("Pleasant Night sir!, Jarvis at Your Command")
    elif 12> t_hour >4:
        speak("Good Morning sir, Jarvis at Your Command")
    elif 18> t_hour >12:
        speak("Good Afternoon sir!, Jarvis at Your Command")
    else:
        speak("Good Evening sir!, Jarvis at Your Command")

greet()


FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())