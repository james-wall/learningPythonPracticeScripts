import re

def isPhoneNumber():
	phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
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
		print('Make sure you enter a valid phone number in your input: ###-###-####')
	else:
		print('Phone number found! ' + result.group())

	print("Goodbye")
		

isPhoneNumber()