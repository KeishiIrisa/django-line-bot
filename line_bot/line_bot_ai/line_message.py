from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import json

REPLY_ENDPOINT_URL = "https://api.line.me/v2/bot/message/reply"
ACCESSTOKEN = ('h46MTdwnnRO+k5/eqMfbrn+Gs2Yxe00yM1yjVHuZkKXGyexng'
               'OS22eibwWO1ZnlUMSRXCW97zc82jS9z04bHv9JCWmCAR4Z918I'
               'l4s53xX0n2Y0EgldMbV6guEDoQvzmtChkK+9DJKLLvDRthx9P9'
               'QdB04t89/1O/w1cDnyilFU=')
HEADER = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + ACCESSTOKEN
}


class LineMessage():
    def __init__(self, messages):
        self.messages = messages

    def reply(self, reply_token):
        body = {
            'replyToken': reply_token,
            'messages': self.messages
        }
        print(body)
        req = urllib.request.Request(
            REPLY_ENDPOINT_URL,
            json.dumps(body).encode(),
            HEADER
        )
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read()
        except urllib.error.HTTPError as err:
            print(err)
        except urllib.error.URLError as err:
            print(err.reason)
