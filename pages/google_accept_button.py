import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class GoogleAcceptButton():
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait
    
    def accept_google_button(self):
        try:
            self.driver.name == 'msedge'
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            inputs = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Jeg accepterer']")))
            inputs.click()
        except Exception as err:
            print('The selected browser is not microsoft edge')
        try:
            google_accept_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Jeg accepterer"]')))
            google_accept_button.click()
        except Exception as err_:
            print('Either run with edge or you are using Data Driven Approach')