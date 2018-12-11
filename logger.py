import logging
import time

logger = logging.getLogger('monitor_log')
logger.setLevel(logging.INFO)

fh = logging.FileHandler('monitor.log')
fh.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)

logger.info('My message in logger')

time.sleep(1.5)
logger.info('My 2nd message in logger')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
