import softest
import inspect
import logging
import pytest
import unittest
from openpyxl import Workbook, load_workbook



class Utils(softest.TestCase):


    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait


    def custom_logger(self, logLevel=logging.DEBUG):
        #set class/method name from where it is called
        logger_name = inspect.stack()[1][3]
        #create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        #create console or filehandler and set the log level
        fh = logging.FileHandler('automation.log', mode='w')
        #create formatter - how you want yuor logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        #add formatter to console or filehandler
        fh.setFormatter(formatter)
        #add console handler to logger
        logger.addHandler(fh)
        return logger

        

    def assertListItemText(self,returned_list):
        bool_expected = True
        retur = 'returrejse'
        count = 1
        for element in returned_list:
            bool_actual = retur in element
            #soft assert - eventhough one element fails in the list-iteration the TC will continue running (Supported by Unittest.Framework)
            self.soft_assert(self.assertEqual, bool_expected, bool_actual)
            if bool_expected == bool_actual:
                print('Item {} {} - {} passed'.format(count,element[6],element[7]))
            else: print('Item {} failed'.format(count))
            count+=1
        self.assert_all()
