# lowermodule.py
import logging.config
import traceback
import time
from pythonjsonlogger import jsonlogger
import logging_tree

def word_count(myfile):
    #logger = logging.getLogger(__name__)
    logger = logging.getLogger('lowermodule')
    logging.config.fileConfig('logging.json.ini', disable_existing_loggers=False)
    print(logger.name)
    logging_tree.printout()
    try:
        starttime = time.time()
        with open(myfile, 'r') as f:
            file_data = f.read()
            words = file_data.split(" ")
            final_word_count = len(words)
            endtime = time.time()
            duration = endtime - starttime 
            logger.info("this file has %d words", final_word_count, extra={"run_duration":duration})
            return final_word_count
    except OSError as e:
        logger.error(e, exc_info=True)
    except:
        logger.error("uncaught exception: %s", traceback.format_exc())
        return False

if __name__ == '__main__':
    word_count('myfile.txt')
