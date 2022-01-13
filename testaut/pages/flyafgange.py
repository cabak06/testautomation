import selenium
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
import pytest
import sys



class FlyAfgange():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def enter_flyafgange(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@jsname='iSelEd'][normalize-space()='Flyafgange'])[1]"))).click()
        except exception as err:
            print('Error can not enter Flyafgange')
