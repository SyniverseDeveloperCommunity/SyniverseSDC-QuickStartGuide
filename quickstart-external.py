# quickstart.py
# tested in python 2.7.12
# implements send SMS example in
# https://sdcdocumentation.syniverse.com/index.php/sms/quick-start
#
# this example can be run using the free credits provided with your account.
# uses one non-standard python library, requests described in detail at
# http://docs.python-requests.org/en/latest/index.html
#
# dependencies are
# 1) SDC account at https://developer.syniverse.com/
# 2) correct service offerings enabled, as described in quick start guide
# 3) application created as descreibed in quick start guide
# 4) whitelisted number, as described in the quick start guide, unless you have added a payment method
#
# changes required to the below script are
# 1) add your access token for the application
# 2) change the channel_id to your preferred one. see list at 
# https://developer.syniverse.com/scg-web-gui/#/main/publicChannels
# 3) change my_number to your whitelisted number
# n.b. for some countries, such as the US, you need to use a pre-existing template

import requests

uk_channel_id = 'DJm-vHcnSBKbeK4b2FAOLQ' # change to your preferred country
my_number = '+44XXXXXXXXXX' # put your UK number here
url = 'https://api.syniverse.com/scg-external-api/api/v1/messaging/message_requests'
sms_text = 'Testing SMS via API!' # change this if you want
access_token = '[YOUR ACCESS TOKEN HERE]'

headers = {'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'}

payload = {'from': 'channel:' + uk_channel_id, 'to': [my_number], 'body': sms_text}

response = requests.post(url, json=payload, headers=headers)

print 'status code: ' + str(response.status_code)
print 'response: ' + response.text
