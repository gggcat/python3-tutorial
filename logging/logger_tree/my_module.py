import logging

def foo():
    logger = logging.getLogger(__name__)
    logger.debug('Debug log message/function')
    logger.info('Info log message/function')
    logger.warning('Warning log message/function')
    logger.error('Error log message/function')

class Bar(object):
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def bar(self):
        self.logger.debug('Debug log message/method')
        self.logger.info('Info log message/method')
        self.logger.warning('Warning log message/method')
        self.logger.error('Error log message/method')