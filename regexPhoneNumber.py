# Method to tell if there is one or more phone numbers is an input string
# Country codes are not supported in this implementation

import re

def isPhoneNumber():
	phoneNumberRegex = re.compile(r'(\d{3})?(-|.)?\d{3}(-|.)?\d{4}')
	result = None
	while(result == None):
		try:
			result = phoneNumberRegex.search(input('Please give us an input string: '))
			if result == None: # the method did not throw, so there is no phone number
				break
		except(TypeError, ValueError) as exception:
			print('Please enter a valid string')

	if result == None:
		print('No phone number found in the input.')
	else:
		print('Phone number found! ' + result.group())
		if len(result.group()) == 7 or len(result.group()) == 8: # No area code
			print('Make sure you add an area code next time!')

	print("Goodbye")
		

isPhoneNumber()