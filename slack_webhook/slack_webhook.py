import os
import json
import requests

class SlackWebHook():
    def __init__(self, webhook_url, user_name, channel):
        self.incoming_webhook_url = webhook_url
        self.user_name = user_name
        self.channel = channel

    def post(self, message):
        post_dic = {
            "text":message,
            "username":self.user_name,
            "icon_emoji":':ghost:',
            "channel":self.channel,
        }

        requests.post(self.incoming_webhook_url, data=json.dumps(post_dic))
        

# Incoming Webhooksを使って対象のチャンネルにメッセージを送付
if __name__=='__main__':
    incoming_webhook_url = os.environ['SLACK_INCOMING_WEBHOOK_URL']
    slack = SlackWebHook(incoming_webhook_url, "JobRunner-BOT", '#report')
    slack.post("テストメッセージ <https://www.google.co.jp>")
