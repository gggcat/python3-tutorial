import os
import json
import logging.config

# 環境変数
mail_from = os.environ['MAIL_FROM']
rcpt_to = os.environ['RCPT_TO']
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = os.environ['SMTP_USER']
smtp_password = os.environ['SMTP_PASSWORD']

# json.load() で読み込むとタプルとリストの区別がつかないので、 json.load()で読み込めない
config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'consoleHandler': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'logging.StreamHandler',
        },
        'smtpHandler': {
            'level': 'ERROR',
            'formatter': 'simple',
            'class': 'logging.handlers.SMTPHandler',
            'mailhost': (smtp_server, smtp_port),
            'fromaddr': mail_from,
            'toaddrs': [rcpt_to],
            'subject': "error log",
            'credentials': (smtp_user, smtp_password),
            'secure': (),
        }
    },
    'loggers': {
        '': {
            'handlers': ['consoleHandler', 'smtpHandler'],
            'level': "INFO",
        }
    }
}

logger = logging.getLogger(__name__)
logging.config.dictConfig(config)
logger.debug('Debug log message')
logger.info('Info log message')
logger.warning('Warning log message')
logger.error('Error log message')
