import logging as logging
import inspect

class CustLogger():

    def cust_logger(self, logLevel=logging.DEBUG):
        #set class/method name from where it is called
        logger_name = inspect.stack()[1][3]
        #create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        #create console or filehandler and set the log level
        fh = logging.FileHandler('automation.log')
        #create formatter - how you want yuor logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        #add formatter to console or filehandler
        fh.setFormatter(formatter)
        #add console handler to logger
        logger.addHandler(fh)
        return logger




