from django.views.debug import ExceptionReporter
from web.settings import SLACK_WEBHOOK_URL, SLACK_ICON
import sys
import requests
import json


class CustomExceptionReporter(ExceptionReporter):
    def get_traceback_text(self):
        text = super().get_traceback_text()
        send_slack_notif(text)
        return text


def send_slack_notif(error_text):
    message = error_text
    title = f"New error :zap:"
    slack_data = {
        "username": "OB Error Bot",
        "icon_emoji": SLACK_ICON,
        "attachments": [
            {
                "color": "#9733EE",
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)

