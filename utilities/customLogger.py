import logging
import os
location=os.getcwd()
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=location,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')  # Corrected date format
        logger = logging.getLogger('tipper')
        logger.setLevel(logging.INFO)
        return logger
