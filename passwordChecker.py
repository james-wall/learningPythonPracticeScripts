#!/usr/bin/python3
# gets a password and checks against it
# NOTE: not very secure because password is hard-coded in, this program is just for learning and testing

correctPassword = 'password123'
numAttempts = 3

while numAttempts > 0:
	password = str(input('Password? '))

	if password == correctPassword:
		print('Password is correct. Access granted')
		# do some stuff
		print('fyi, you need a better password')
		break
	else:
		print('Password incorrect. Access denied')
		numAttempts = numAttempts - 1
		if numAttempts > 0:
			print('Please try again. ' + str(numAttempts) + ' remaining.')
		else:
			print('You have used up all of your attempts to enter the correct password. You are locked out of this account until further notice.')

# Signing off
print('Goodbye')