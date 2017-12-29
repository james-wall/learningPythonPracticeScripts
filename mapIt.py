#! c:\Python36-32\python3.exe
# launches a map in the browser using an address from the command line or clipboard
# inspired by ATBSWP

import sys
# print(sys.version) # only use when debugging

import requests, logging, argparse, webbrowser, pyperclip

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-l','--locations', help='Use this argument to indicate if you want the location of the input', nargs='+', required=False)
parser.add_argument('-d','--directions', help='Use this argument to indicate if you want directions to the input locations from your current location', nargs='+', required=False)
parser.add_argument('-s','--searchArea', help='Use this argument to indicate if you want to search nearby for things', nargs='+', required=False)

args = parser.parse_args()

logging.debug("before if statements")

if args.directions:
	logging.debug("directions is true")
	# check number of command line arguments
	if len(args.directions) > 0:
		# get address from command line arguments
		address = ' '.join(args.directions)
	else:
		# Get address from clipboard
		address = pyperclip.paste()

	# get user's current location.. TODO needs work on accuracy
	freegeoip = "http://freegeoip.net/json"
	geo_r = requests.get(freegeoip)
	geo_json = geo_r.json()

	webbrowser.open('https://www.google.com/maps/dir/' + str(geo_json["latitude"]) + ',' + str(geo_json["longitude"]) + '/' + address)
elif args.locations:
	# check number of command line arguments
	if len(args.locations) > 0:
		# get address from command line arguments
		address = ' '.join(args.locations[0:])
	else:
		# Get address from clipboard
		address = pyperclip.paste()
	webbrowser.open('https://www.google.com/maps/place/' + address)
elif args.searchArea:
	# check number of command line arguments
	if len(args.searchArea) > 0:
		# get address from command line arguments
		address = ' '.join(args.searchArea)
	else:
		# Get address from clipboard
		address = pyperclip.paste()
		print(address)

	# get user's current location.. TODO needs work on accuracy
	freegeoip = "http://freegeoip.net/json"
	geo_r = requests.get(freegeoip)
	geo_json = geo_r.json()
	webbrowser.open('https://www.google.com/maps/search/' + address + '/' + str(geo_json["latitude"]) + ',' + str(geo_json["longitude"]) + '/')

logging.debug("end of program")