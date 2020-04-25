import os
import logging
from slack_log_handler import SlackLogHandler
# https://github.com/claudetech/python-slack-log

WEBHOOK_URL = os.getenv('SLACK_INCOMING_WEBHOOK_URL')

slack_handler = SlackLogHandler(WEBHOOK_URL)
slack_handler.setLevel(logging.WARNING)

logger = logging.getLogger(__name__)
logger.addHandler(slack_handler)

logger.error('Oh my god, an error occurred!')