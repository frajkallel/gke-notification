import json

from httplib2 import Http

import os

import base64


def main(event, context):
    """Google Chat incoming webhook quickstart."""
    url = os.environ.get("WEBHOOK_URL")
    notif = json.dumps(event,indent=4)
    notifs = notif.replace("\\","")
    app_message = {'text': '```'+ notifs + '```'}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=json.dumps(app_message),
    )
    print(response)
