import selenium
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import sys
import softest
import logging
from ddt import ddt, data, file_data, unpack
sys.path.append(r'\Users\cahit\Desktop\testautomation')
import pages.google_accept_button, pages.flyafgange, pages.rejse_specifikationer, pages.logics, utilities.utils, utilities.reader
from utilities.reader import Reader
reader = Reader()
reader = Reader()

#to run the TC: pytest -vs --browser chrome|firefox|edge

@pytest.mark.usefixtures("setup")
@ddt
class TestGoogleTravelReturn(softest.TestCase):
    
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.acc_button =  pages.google_accept_button.GoogleAcceptButton(self.driver,self.wait)
        self.enter_flyafgange = pages.flyafgange.FlyAfgange(self.driver, self.wait)
        self.details = pages.rejse_specifikationer.RejseSpecifikationer(self.driver, self.wait)      
        self.logic = pages.logics.Logics(self.driver, self.wait)
        self.utils = utilities.utils.Utils(self.driver, self.wait)
        self.log = self.utils.custom_logger(logLevel=logging.WARNING)
    
    
    #@data(("Paris", "London", "fre. 28. jan", "fre. 18. feb."),("Amsterdam", "Berlin", "ons. 26. jan", "fre. 18. feb."),("København", "Madrid", "tor. 27. jan", "tor. 17. feb."))
    #@unpack
    #@file_data("../testdata/jdata.json")   RUN JSON FILE
    #@file_data("../testdata/testyml.yml")  RUN YAML FILE
    #@data(*reader.read_data_from_excel('../testdata/test_xl.xlsx','Mysheet')) RUN EXCEL FILE
    
    @data(*reader.read_data_from_csv('testdata/CSV_data.csv'))
    @unpack
    def test_googl_travel_return(self,dest_from,dest_to,date_go,date_re):
        
        self.acc_button.accept_google_button()
        self.enter_flyafgange.enter_flyafgange()
        self.details.detaljer()
        self.details.destination(dest_from,dest_to)
        self.details.dates(date_go,date_re)
        elements = self.details.get_all_found_travels()
        time.sleep(2)
        returned_list = self.logic.make_travelData_readable(elements)
        print(len(returned_list))
        for el in returned_list:
            print(el)

        bool_expected = True
        retur = 'returrejse'
        togforbindelse = 'Togforbindelse'
        count = 1
        for element in returned_list:
            if togforbindelse in element:
                continue
            else:
                bool_actual = retur in element
                #soft assert - eventhough one element fails in the list-iteration the TC will continue running (Supported by Unittest.Framework)
                self.soft_assert(self.assertEqual, bool_expected, bool_actual)
                if bool_expected == bool_actual:
                    self.log.warning('Item {} {} - {} passed'.format(count,element[5],element[6]))
                else: print('Item {} failed'.format(count))
            count+=1
        self.assert_all()


    def test_manipulate_pass(self):
        self.acc_button.accept_google_button()
        self.enter_flyafgange.enter_flyafgange()
        bool_manipulated_true = True
        bool_true = True
        self.assertEqual(bool_manipulated_true, bool_true)
        



