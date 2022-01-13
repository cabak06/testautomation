#url = https://www.youtube.com/watch?v=FFDDN1C1MEQ&list=PLKDS9KgTO3TnRpPH_DuiForAy2Wh0Ugnh
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_path = 'drivers\chromedriver.exe'
driver_path2 = 'chromedriver.exe'

google_url = 'https://www.google.com'
driver = webdriver.Chrome(driver_path2)

driver.get(google_url)
driver.maximize_window()
driver.implicitly_wait(5)
#list_ = driver.find_elements_by_class_name('QS5gu sy4vM')
#submit_button = list_[1].click()

driver.find_element_by_xpath('//button[normalize-space()="Jeg accepterer"]').click()
#submit_button = list_.click()
driver.implicitly_wait(3)

driver.find_element_by_name("q").send_keys("Automation Step by Step", Keys.RETURN)
#driver.find_element_by_name("q").send_keys("Automation Step by Step")
#driver.find_element_by_name("btnK").send_keys(Keys.RETURN)
driver.implicitly_wait(5)

#//*[@id="L2AGLb"]/div

