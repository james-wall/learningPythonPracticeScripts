#! c:\Python36-32\python3.exe
# Gets top results from Google search and opens new tabs for each of them
# inspired by ATBSWP

import sys
# print(sys.version) # only use when debugging

import bs4, requests, logging, argparse, webbrowser, pyperclip

print('Googling now...')

if len(sys.argv) > 0:
		# get address from command line arguments
		address = ' '.join(sys.argv[1:])
else:
	# Get address from clipboard
	address = pyperclip.paste()

res = requests.get('https://www.google.com/search?q=' + str(address))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

elems = soup.select(".r a")

numOpen = min(5, len(elems)) # currently opens max of 5 tabs
for i in range(numOpen):
	webbrowser.open('http://google.com' + elems[i].get('href'))
