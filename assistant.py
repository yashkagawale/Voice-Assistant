import speech_recognition as sr
import pyttsx3
import cv2
import datetime
import os
import requests
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
r = sr.Recognizer()


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def take_command():
    with sr.Microphone as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")
    except:
        return "  "
    query = query.lower()
    return query


def wish():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour <= 12:
        speak("Good Morning")
    elif 12 < hour < 18:
        speak("Good Afternoon ")
    else:
        speak("Good Evening")


if __name__ == "__main__":
    wish()
    while True:

        query = take_command().lower()

        if "hey" or "hi" in query:
            speak("Hi.It's good to hear from you")

        elif "thank you" in query:
            speak("shukriyaa to you")

        elif "open notepad" in query:
            path = "C:\\WINDOWS\\system32\\notepad.exe"
            speak('opening notepad')
            os.startfile(path)

        elif "close notepad" in query:
            speak("closing notepad")
            os.system("TASKKILL /PID notepad.exe /T")

        elif "camera" in query:
            speak("opening camera")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "ip address" in query:
            ip = requests.get('https://api.ipify.org').text
            speak("Your ip address is " + ip)
        else:
            speak("please say it again.")

