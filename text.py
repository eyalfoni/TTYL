from __future__ import print_function
from twilio.rest import Client
import os

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')

client = Client(account_sid, auth_token)


def send_text(doc):
    to_number = doc['sending_num']
    message = doc['msg']
    twil_message = client.api.account.messages.create(to=to_number,
                                                      from_=TWILIO_NUMBER,
                                                      body=message)
    print(twil_message)
