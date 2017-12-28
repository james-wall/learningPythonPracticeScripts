#! c:\Python36-32\python3.exe
# launches a map in the browser using an address from the command line or clipboard
# inspired by ATBSWP

import sys
# print(sys.version) # only use when debugging

import webbrowser, pyperclip

# check number of command line arguments
if len(sys.argv) > 1:
	# get address from command line arguments
	address = ' '.join(sys.argv[1:])
else:
	# Get address from clipboard
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)