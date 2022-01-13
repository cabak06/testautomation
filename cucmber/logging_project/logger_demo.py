import logging


class LoggerDemo():

    def sample_logger_console(self):
        #create logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        #create console handler or filehandler and set the log-level
        console_handler = logging.StreamHandler()
        #create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        #add formatter to console or filehandler
        console_handler.setFormatter(formatter)
        #add console handler to logger
        logger.addHandler(console_handler)
        #application code - log messages
        logger.debug('this is debug')
        logger.info('this is info')
        logger.warning("this is warning")
        logger.error('this is error')
        logger.critical('this issss critical')



    def sample_logger_file(self):
        #create logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        #create filehandler and set the log-level
        file_handler = logging.FileHandler(filename='MY_LOGS.log')
        #create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        #add formatter to console or filehandler
        file_handler.setFormatter(formatter)
        #add console handler to logger
        logger.addHandler(file_handler)
        #application code - log messages
        logger.debug('this is debug')
        logger.info('this is info')
        logger.warning("this is warning")
        logger.error('this is error')
        logger.critical('this issss critical')


ld = LoggerDemo()
ld.sample_logger_file()


