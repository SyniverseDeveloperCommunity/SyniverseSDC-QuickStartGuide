# quickstart.py
# tested in python 2.7.12
# implements send SMS example in
# https://sdcdocumentation.syniverse.com/index.php/sms/quick-start

import requests

uk_channel_id = 'DJm-vHcnSBKbeK4b2FAOLQ'
my_number = '+44XXXXXXXXXX' # put your UK number here
url = 'https://api.syniverse.com/scg-external-api/api/v1/messaging/message_requests'
sms_text = 'Testing SMS via API!'
access_token = '[YOUR ACCESS TOKEN HERE]'

headers = {'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'}

payload = {'from': 'channel:' + uk_channel_id, 'to': [my_number], 'body': sms_text}

response = requests.post(url_int, json=payload, headers=headers)

print 'status code: ' + str(response.status_code)
print 'response: ' + response.text
