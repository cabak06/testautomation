import selenium
from selenium import webdriver
import time
import env
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


def test_explicit_wait():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(By.XPATH, "")).click()   




class WebCrawlers():

    def __init__(self):
        pass

    def login_to_codingbat(self):
        url_codingbat = "https://codingbat.com/python"
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as err:
            print('could not get driver')
        driver.get(url_codingbat)
        time.sleep(5)
        driver.maximize_window()
        driver.implicitly_wait(5)
        time.sleep(3)
        driver.find_element_by_xpath("//a[normalize-space()='Java']").click()
        time.sleep(3)
        input_id_email = driver.find_element_by_xpath("//input[@name='uname']")
        input_id_email.send_keys(env.login_id)
        time.sleep(3)
        input_pass = driver.find_element_by_xpath("//input[@name='pw']")
        input_pass.send_keys(env.password)
        time.sleep(3)
        driver.find_element_by_xpath("//input[@name='dologin']").click()
        time.sleep(4)
        driver.save_screenshot('screenshots.png')


    def checkbox_and_radiobutton(self):
        url = "https://www.sugarcrm.com/"
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as err:
            print('could not get driver')
        driver.get(url)
        time.sleep(5)
        driver.maximize_window()
        driver.implicitly_wait(5)
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/div[2]/div/button").click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//a[@href='https://www.sugarcrm.com/uk/request-demo/']//span[@class='ubermenu-target-title ubermenu-target-text'][normalize-space()='Get a Demo']").click()
        time.sleep(3)
        #check box
        driver.find_element_by_id("interest_market_c0").click()
        time.sleep(2)
        driver.find_element_by_id("interest_sell_c0").click()
        time.sleep(2)
        driver.find_element_by_id("interest_serve_c0").click()
        time.sleep(2)
        #radiobutton
        driver.find_element_by_id("doi0").click()
        time.sleep(2)
        driver.find_element_by_id("doi1").click()
        time.sleep(2)


    def dropdown_single_select(self):
        url = "https://www.salesforce.com/"
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as err:
            print('could not get driver')
        driver.get(url)
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_id("onetrust-accept-btn-handler").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[normalize-space()='Try For Free']").click()
        time.sleep(2)
        handles = driver.window_handles
        for handle in handles:
            driver.switch_to.window(handle)
            try:
                drp_employee = driver.find_element_by_name("CompanyEmployees")
                drp_country = driver.find_element_by_name("CompanyCountry")
                drp_language = driver.find_element_by_name("CompanyLanguage")
                time.sleep(2)
                if drp_employee and drp_country and drp_language:                        
                        drp_emp = Select(drp_employee)
                        drp_emp.select_by_value("150")
                        time.sleep(2)
                        drp_cou = Select(drp_country)
                        drp_cou.select_by_value("PA")
                        time.sleep(2)
                        drp_lan = Select(drp_language)
                        drp_lan.select_by_value("es")
            except Exception as err:
                print('could not find the required path for element with windpwshandlerID = ', handle)


    def multi_select(self):
        url = 'http://makeseleniumeasy.com/2017/08/18/part-1-handling-drop-down-created-using-select-tag-in-selenium/#Multi_select_dropdown_example'
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as err:
            print('could not get driver')
        driver.get(url)
        driver.maximize_window()
        multi = driver.find_element_by_xpath("//select[2]")
        multiliners = Select(multi)
        multiliners.select_by_value("English")
        multiliners.select_by_value("Kannada")
        multiliners.select_by_index(3)
        time.sleep(10)



    def auto_complete(self,place_depart,date_depart,date_return):
        """This method is a webcrawler and searches google travel for destination based on input params: depart/return dates/places.
           param date_depart: depart date type - STRING, must be in format "man. 10. jan" (day. monthNum. month.)
           param date_retun:  return date type - STRING, must be in format "man. 10. jan" (day. monthNum. month.)
           return: Metadata containing the cheapest flight-info.  
        """
        t1 = time.sleep(1) 
        t2 = time.sleep(2)
        t3 = time.sleep(3)
        t4 = time.sleep(4)
        #, paramStart, paramEnd
        """This medhod rakes two params. 
        paramStart is takeoff for flight.
        paramEnd is end destionation for flight
        """
        url = "https://www.google.com/travel/"
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as err:
            print('could not get driver')        
        driver.get(url)
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_xpath('//button[normalize-space()="Jeg accepterer"]').click()
        time.sleep(2)
        #click flights
        driver.find_element_by_xpath("//div[@class='PH4Kgc']//span[@jsname='iSelEd'][normalize-space()='Flyafgange']").click()
        time.sleep(4)
        #adhjusting place,date for flights
        driver.find_element_by_xpath("//button[@aria-label='1 passager, rediger antallet af passagerer.']//span[@class='VfPpkd-kBDsod UmgCUb']//*[name()='svg']").click()
        driver.find_element_by_xpath("//button[@aria-label='Tilføj voksen']//*[name()='svg']").click()
        driver.find_element_by_xpath("//button[@class='VfPpkd-LgbsSe ksBjEc lKxP2d bRx3h']//span[@class='VfPpkd-vQzf8d'][normalize-space()='Udfør']").click()
        try:
            field = driver.find_element_by_xpath("//input[@value='København']").click()
            time.sleep(3)
        except Exception as err:
            print("no field København")    
        try:
            field_ = driver.find_element_by_xpath("//input[@value='Aarhus']").click()
            time.sleep(3)
        except Exception as err:
            print("No field Aarhus")    

        find_dest = driver.find_element_by_xpath("//div[@aria-label='Angiv dit afrejsested']//div//input[@aria-label='Hvor ellers?']")
        #find_dest.send_keys("London")
        #find_dest.send_keys("Helsinki")
        time.sleep(3)
        #driver.find_element_by_xpath("//div[normalize-space()='London Heathrow Airport']").click()
        driver.find_element_by_xpath("(//div[normalize-space()='Helsinki Lufthavn'])[1]").click()
        t2
        ##
        driver.find_element_by_xpath("//input[@placeholder='Hvor vil du hen?']").click()
        time.sleep(3)
        vv = driver.find_element_by_xpath("//div[@aria-label='Angiv din destination']//div//input[@aria-label='Hvor ellers?']")
        vv.send_keys("Ankara")
        time.sleep(3)
        driver.find_element_by_xpath("//div[contains(text(),'Esenboğa Internationale Lufthavn')]").click()
        t3
        #driver.find_element_by_xpath("(//*[name()='svg'][contains(@class,'NMm5M')])[47]").click()   
        driver.find_element_by_xpath("(//input[@placeholder='Afrejsedato'])[1]").click()
        t3
        afrejse_dato = driver.find_element_by_xpath("(//input[contains(@placeholder,'Afrejsedato')])[2]")
        t3
        afrejse_dato.send_keys(date_depart, Keys.RETURN)
        t3
        driver.find_element_by_xpath("(//*[name()='svg'][contains(@class,'PtrSMb NMm5M hhikbc')])[8]").click()
        #driver.find_element_by_xpath("(//input[contains(@placeholder,'Hjemrejsedato')])[2]").click()
        t3
        hjemkomst = driver.find_element_by_xpath("(//input[@placeholder='Hjemrejsedato'])[2]")
        hjemkomst.send_keys(date_return, Keys.RETURN)
        t4
        driver.find_element_by_xpath("(//span[contains(@class,'VfPpkd-vQzf8d')][normalize-space()='Udfør'])[2]").click()
        time.sleep(10)
        driver.find_element_by_xpath("//span[@class='bEfgkb']").click()
        time.sleep(6)
        #driver.find_element_by_xpath("(//*[name()='svg'][@class='XWBoJb NMm5M'])[1]").click()
        #driver.find_element_by_class_name("XWBoJb NMm5M").click()
        driver.find_element_by_xpath("(//span[@class='bEfgkb'])[1]").click()
        time.sleep(10)
        elements = driver.find_elements_by_class_name("KC3CM")
        time.sleep(5)
        elements_list = []
        for element in range(len(elements)):
            time.sleep(2)
            elements_list.append(elements[element].text)
        listed = []
        for i in elements_list:
            line = i.splitlines()
            listed.append(line)
        
        cheapest_match = []
        string_code = "kr."
        price = 100000
        for lst in listed:
            for element in lst:
                if element[-3:] == string_code:
                    money_field = element.split(" ")
                    tmp_price = float(money_field[0])
                    if tmp_price < price:
                        print("tmp price ", tmp_price, " price ", price)
                        price = tmp_price
                        cheapest_match.clear()
                        cheapest_match.append(lst)
        print(cheapest_match)
        return cheapest_match
  

    def scrape(self):
        url = "https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDFsZnkSCjIwMjItMDMtMDRyBwgBEgNFU0IaI2oHCAESA0VTQhIKMjAyMi0wNC0yMnIMCAMSCC9tLzAxbGZ5cAGCAQsI____________AUABSAGYAQE"
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as err:
            print('could not get driver')        
        driver.get(url)
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_xpath('//button[normalize-space()="Jeg accepterer"]').click()
        time.sleep(2)
        driver.find_element_by_xpath("(//*[name()='svg'][@class='XWBoJb NMm5M'])[1]").click()
    
        time.sleep(2)
        elements = driver.find_elements_by_class_name("KC3CM")
        time.sleep(5)
        elements_list = []
        for element in range(len(elements)):
            time.sleep(2)
            elements_list.append(elements[element].text)
        listed = []
        for i in elements_list:
            line = i.splitlines()
            listed.append(line)

        cheapest_match = []
        price = 100000.00
        for lst in listed:
            cut_element = lst[11]
            money_field = cut_element.split(" ")
            tmp_price = float(money_field[0])
            if tmp_price < price:
                price = tmp_price
                cheapest_match.clear()
                cheapest_match.append(lst)
        print(cheapest_match)
        return cheapest_match
    
            
        driver.find_element_by_xpath("(//*[name()='svg'][@class='XWBoJb NMm5M'])[1]").click()
        time.sleep(2)
        elements = driver.find_elements_by_class_name("KC3CM")
        time.sleep(5)
        elements_list = []
        for element in range(len(elements)):
            time.sleep(2)
            elements_list.append(elements[element].text)
        listed = []
        for i in elements_list:
            line = i.splitlines()
            listed.append(line)

        cheapest_match = []
        price = 100000.00
        for lst in listed:
            cut_element = lst[11]
            money_field = cut_element.split(" ")
            tmp_price = float(money_field[0])
            if tmp_price < price:
                price = tmp_price
                cheapest_match.clear()
                cheapest_match.append(lst)
        print(cheapest_match)
        return cheapest_match            


        
    def capture_screenshot(self):
        # I'm using the login to coding-bat method as an example to capture screenshot
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as err:
           print('could not get driver')   
        url_codingbat = "https://codingbat.com/python"
        driver.get(url_codingbat)
        #self.login_to_codingbat()
        time.sleep(2)
        click_warmUP = driver.execute_script("return document.getElementsByTagName('a')[11]")
        time.sleep(2)
        click_warmUP.click()
        time.sleep(2)
        driver.save_screenshot(r'C:\\Users\\cahit\\Desktop\\scr.png')

        
    def handle_alerts(self):
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as err:
           print('could not get driver')  
        url = 'https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert'
        driver.get(url)
        time.sleep(3)
        driver.find_element_by_id('accept-choices').click()
        time.sleep(3)
        driver.maximize_window()
        time.sleep(2)
        driver.switch_to.frame("iframeResult")
        time.sleep(2)
        driver.find_element_by_xpath("//button[normalize-space()='Try it']").click()
        time.sleep(3)
        alert_text = driver.switch_to.alert.text
        print(alert_text)
        driver.switch_to.alert.accept()


    def handle_mouse_hover(self):
        url = 'https://www.toolsqa.com/'
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as err:
            print('could not get driver')  
        driver.get(url)
        driver.maximize_window()
        time.sleep(2)

        driver.find_element_by_id('accept-cookie-policy').click()
        time.sleep(2)
        driver.find_element_by_class_name('navbar__tutorial-menu--text').click()
        time.sleep(2)
        #Creating an object of actionChange class so I can make mouse-hovering
        achains = ActionChains(driver)
        element_to_hover = driver.find_element_by_xpath("//span[normalize-space()='Back-End Testing Automation']")
        achains.move_to_element(element_to_hover).perform()
        time.sleep(2)
        driver.find_element_by_xpath("//ul[@class='active']//a[@title='SOAPUI'][normalize-space()='SOAPUI']").click()
        time.sleep(2)
        #Rightclicking using actionChain - context_click
        element_to_right_click = driver.find_element_by_xpath("//span[@class='navbar__tutorial-menu--text']")
        achains.context_click(element_to_right_click).perform()
        time.sleep(2)

    def test_right_click(self):
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as err:
           print('could not get driver')   
        url = 'http://demo.guru99.com/test/simple_context_menu.html'
        driver.get(url)
        time.sleep(1)
        driver.maximize_window()
        time.sleep(5)
        iframe = driver.find_element_by_class_name("faktor-iframe-wrapper")
        driver.switch_to.frame(iframe)
        time.sleep(2)
        driver.find_element_by_xpath('//button[normalize-space()="Afvis alle"]').click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[normalize-space()='Afvis']").click()
        driver.switch_to.default_content()
        achains = ActionChains(driver)
        elR = driver.find_element_by_xpath("//span[@class='context-menu-one btn btn-neutral']")
        achains.context_click(elR)
        double_click = driver.find_element_by_xpath("//button[normalize-space()='Double-Click Me To See Alert']")
        achains.double_click(double_click).perform()
        time.sleep(2)

    def handling_sliders(self):
        url = 'https://www.snapdeal.com/products/mobiles?sort=plrty'
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as err:
           print('could not get driver') 
        driver.get(url)
        driver.maximize_window()
        time.sleep(2)
        elem_left = driver.find_element_by_xpath("//a[contains(@class, 'left-handle')]")
        elem_right = driver.find_element_by_xpath("//a[contains(@class, 'right-handle')]")
        ActionChains(driver).drag_and_drop_by_offset(elem_left, 90, 0).perform()
        time.sleep(3)
        ActionChains(driver).drag_and_drop_by_offset(elem_right, -50, 0).perform()
        time.sleep(3)
        #elements = driver.find_elements_by_class_name('col-xs-6  favDp product-tuple-listing js-tuple ')
        elements = driver.execute_script("return document.getElementsByClassName('col-xs-6  favDp product-tuple-listing js-tuple ')");
        time.sleep(5)
        elements_list = []
        for element in range(len(elements)):
            time.sleep(2)
            elements_list.append(elements[element].text)

        for i in elements_list:
            print(i)
        #listed = []
        #for i in elements_list:
        #    line = i.splitlines()
        #    listed.append(line)








#auto_complete = WebCrawlers()
#auto_complete.dropdown_single_select()
#auto_complete.login_to_codingbat()
#auto_complete.auto_complete("London","tir. 28. dec.","lør. 29. jan.")
#multi_s = WebCrawlers()
#multi_s.multi_select()
#d_down = WebCrawlers()
#d_down.dropdown_single_select()
#checkbox = WebCrawlers()
#checkbox.checkbox_and_radiobutton()
#aa = WebCrawlers()
#aa.login_to_codingbat()s
#WebCrawlers().capture_screenshot()
#WebCrawlers().handle_alerts()
#WebCrawlers().handle_mouse_hover()
#WebCrawlers().test_right_click()
WebCrawlers().handling_sliders()
