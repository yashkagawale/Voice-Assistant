import sys
import speech_recognition as sr
import datetime
import os
import requests
import cv2
import pyautogui
import wikipedia
import webbrowser
from features import *
import instaloader
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
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
    speak("I am luci")


def news():
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=f402164ccf374ca4bdbcca0e1dfc64d3"

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["1", "2", "3", "4", "5", "6", ]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"Number {day[i]} news is:{head[i]}")


if __name__ == "__main__":
    # wish()
    while True:
        # if 1:
        speak("Tell me how can I help you now?")
        query = take_command().lower()

        if "google" in query:
            speak("what should I search on google ?")
            tell = take_command()
            w = tell.replace("what is", "")
            v = tell.replace("who is", "")
            speak('Searching information related to {} on google'.format(v).format(w))

            assist = search()
            assist.click(tell)

        elif "wikipedia" in query:
            speak("sure, You need information related to which topic ? ")
            tell = take_command()
            x = tell.replace("what is", "")
            y = tell.replace("who is", "")
            speak('Searching {} in wikipedia'.format(x).format(y))
            talk = wikipedia.summary(tell, 3)

            assist = info()
            assist.get_info(tell)
            speak("According to wikipedia")
            speak(talk)

        elif "open notepad" in query:
            path = "C:\\WINDOWS\\system32\\notepad.exe"  #
            speak('opening notepad')
            os.startfile(path)

        elif "close notepad" in query:
            speak("closing notepad")
            os.system("TASKKILL /PID notepad.exe /T")  # TASKKILL /PID scad3.exe /T taskkil /f /im notepad.exe

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

        elif "thank you" in query:
            speak("No problem")
            speak("shukriyaa to you")

        elif "news" in query:
            speak("Fetching latest news, wait a moment")
            news()

        elif "devotional songs" in query:
            speak("Playing devotional songs")
            music_dir = "D:\\MUSIC\\ganpati-songs"
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith(".mp3"):
                    os.startfile(os.path.join(music_dir, song))
            sys.exit()

        elif "workout" in query:
            speak("Get ready to burn calories")
            speak("Here we go!")
            music_dir = "D:\\MUSIC\\workout-songs"
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith(".mp3"):
                    os.startfile(os.path.join(music_dir, song))
            sys.exit()

        elif "party" in query:
            speak("Playing party songs")
            music_dir = "D:\\MUSIC\\party-songs"
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith(".mp3"):
                    os.startfile(os.path.join(music_dir, song))
            sys.exit()

        elif "ip address" in query:
            ip = requests.get('https://api.ipify.org').text
            speak("Your ip address is " + ip)

        elif "youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening youtube")

        elif "mail" in query:
            webbrowser.open("https://mail.google.com")
            speak("Opening google gmail")

        elif "facebook" in query:
            webbrowser.open("https://www.facebook.com")
            speak("Opening facebook")

        elif "stack overflow" in query:
            webbrowser.open("https://www.stackoverflow.com")
            speak("Opening stack overflow")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")

        elif "where i am" in query:
            speak("wait, let me check")
            try:
                ip = requests.get("https://api.ipify.org").text
                print(ip)
                url = "https://get.geojs.io/v1/ip/geo/" + ip + ".json"
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                # state = geo_data['state']
                country = geo_data['country']
                speak(f"I am not sure, but i think we are in {city} city of {country}")
            except Exception as e:
                speak("due to network issue i am not able to find")
                pass

        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = take_command()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            time.sleep(3)
            speak("i am done sir, the screenshot is saved in our main folder.")

        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("sir please tell me you want to hide this folder or make it visible for everyone")
            condition = take_command()
            if "hide" in condition:
                os.system("attrib th /s /d")  # os module
                speak("sir, all the files in this folder are now hidden.")
            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("sir, all the files in this folder are now visible to everyone.")
            elif "leave it" in condition or "leave for now" in condition:
                speak("Ok sir")

        elif "instagram profile" or "profile on instagram" in query:
            speak("please enter the user name correctly.")
            name = input("Enter username here: ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak("Here is the instgram profile of {}".format(name))
            time.sleep(3)
            speak("Would you like to download profile picture of account")
            condition = take_command()
            if "yes" in query:
                mod = instaloader.instaloader()  # pip install instadownloader
                mod.download_profit(name, profile_pic_only=True)
                speak("I am done, profile picture is saved in our main folder.")
            else:
                pass

        elif "video" in query:
            speak("which video you want to play ?")
            query = take_command()
            v = query.replace("paly", "")
            speak("Playing {} on youtube".format(v))

            assist = video()
            assist.play(v)

        else:
            speak("please say it again.")

        # speak("Do you have any other work for me")
