from pyautogui import click
from selenium import webdriver
import pyttsx3



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id) 
engine.setProperty('rate', 170)


def speak(audio):
   print("  ")
   print(f": {audio}")
   print("  ")
   engine.say(audio)
   engine.runAndWait()
   print("  ")

class video():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\Windows\chromedriver_win32\chromedriver.exe')

    def play(self, query):
        self.query = query
        self.driver.get(url='https://www.youtube.com/results?search_query=' + query)
        video = self.driver.find_element_by_xpath('//*[@id="video-title"]')
        video.click()

class search():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\Windows\chromedriver_win32\chromedriver.exe')

    def click(self, query):
        self.query = query
        self.driver.get(url='https://www.google.com/search?q=' + query)
        search = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input')
        return search

class info():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\Windows\chromedriver_win32\chromedriver.exe')

    def get_info(self, query):
        self.query = query
        self.driver.get('http://www.wikipedia.org')
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()
