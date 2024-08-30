from selenium import webdriver


class search:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\Windows\chromedriver_win32\chromedriver.exe')

    def click(self, query):
        self.query = query
        self.driver.get(url='https://www.google.com/search?q=' + query)
        search = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input')
        return search