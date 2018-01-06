#! C:\Python36-32\python3.exe
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.
# inspired by ATBSWP

# Preset values:
accountSID = ''
authToken = ''
twilioNumber = ''

toNumbers = {
	
	}

import sys
from twilio.rest import Client

twilioCli = Client(accountSID, authToken)

sendText = True

if len(sys.argv) == 2:
	toPerson = sys.argv[1]
	strToPerson = str(toPerson)
	message = str(input('What do you want to say to ' + strToPerson + '? '))
elif len(sys.argv) > 2:
	toPerson = sys.argv[1]
	strToPerson = str(toPerson)
	message = ' '.join(sys.argv[2:])
else:
	print("Invalid arguments.")
	print("Please try again format your arguments as one of the following: ")
	print("text personName")
	print("OR")
	print("text personName message")
	sendText = False

if sendText:
	print('Sending text to ' + strToPerson)
	twilioCli.messages.create(body=message, from_=twilioNumber, to=toNumbers.get(strToPerson))
	print('Text sent')