import selenium
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class RejseSpecifikationer():
    
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def detaljer(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='1 passager, rediger antallet af passagerer.']//span[@class='VfPpkd-kBDsod UmgCUb']//*[name()='svg']"))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Tilføj voksen']//*[name()='svg']"))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='VfPpkd-LgbsSe ksBjEc lKxP2d bRx3h']//span[@class='VfPpkd-vQzf8d'][normalize-space()='Udfør']"))).click()
        except Exception as err:
            print('Seems there already have benne selected double passengers')



    def destination(self,dest_from,dest_to):

        try:
            elems = self.driver.execute_script("return document.getElementsByClassName('II2One j0Ppje zmMKJ LbIaRd')")
            elem_departure = elems[0]
            self.wait.until(EC.element_to_be_clickable(elem_departure)).click()
        except Exception as err:
            print("no elems to click")    

        find_dest = self.driver.find_element_by_xpath("//div[@aria-label='Angiv dit afrejsested']//div//input[@aria-label='Hvor ellers?']")
        find_dest.send_keys(dest_from, Keys.RETURN)
 
        elem_arrival = elems[2]
        self.wait.until(EC.element_to_be_clickable(elem_arrival)).click()
        depart_to = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Angiv din destination']//div//input[@aria-label='Hvor ellers?']")))
        depart_to.send_keys(dest_to, Keys.RETURN)


    def dates(self,date_go,date_re):
        dates_specs = self.driver.execute_script("return document.getElementsByClassName('RKk3r eoY5cb j0Ppje')")
        dates_depart = dates_specs[0]
        dates_return = dates_specs[1]

        dates_depart.click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[normalize-space()='Nulstil'])[1]"))).click()

        time.sleep(2)
        afrejse_dato = self.driver.find_element_by_xpath("(//input[@placeholder='Afrejsedato'])[2]")
        hjemrejse_dato = self.driver.find_element_by_xpath("(//input[@placeholder='Hjemrejsedato'])[2]")
   
        self.wait.until(EC.element_to_be_clickable(afrejse_dato)).click()
        afrejse_dato.send_keys(date_go, Keys.ENTER)
        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable(hjemrejse_dato)).click()
        hjemrejse_dato.send_keys(date_re, Keys.RETURN)
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(@class,'VfPpkd-vQzf8d')][normalize-space()='Udfør'])[2]"))).click()

    def get_all_found_travels(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='bEfgkb']"))).click()
        time.sleep(2)
        elements = self.driver.find_elements_by_class_name("KC3CM")
        return elements