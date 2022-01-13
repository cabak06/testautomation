import selenium
from selenium.webdriver.support.ui import WebDriverWait

class Logics():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    def make_travelData_readable(self, elements):
        elements_list = []
        for element in range(len(elements)):
            elements_list.append(elements[element].text)
        listed = []
        for i in elements_list:
            line = i.splitlines()
            listed.append(line)
        return listed