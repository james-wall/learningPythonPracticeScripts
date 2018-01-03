#! C:\Python36-34\python3.exe
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.

import requests, os, bs4, threading
os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd

def downloadXkcd(startComic, endComic):
	for urlNumber in range(startComic, endComic):
		if urlNumber == 400:
			print('Haha, very funny XKCD.. Page 404 returns a 404 error so we are skipping it')
			continue

		# Download the page.
		print('Downloading page http://xkcd.com/%s...' % (urlNumber))
		res = requests.get('http://xkcd.com/%s' % (urlNumber))
		res.raise_for_status()

		soup = bs4.BeautifulSoup(res.text, "html.parser")

		# Find the URL of the comic image.
		comicElem = soup.select('#comic img')
		if comicElem == []:
			print('Could not find comic image.')

		else:
			comicUrl = "https:"
			comicUrl += comicElem[0].get('src')
			# Download the image.
			print('Downloading image %s...' % (comicUrl))
			res = requests.get(comicUrl)
			res.raise_for_status()

			try:
				# Save the image to ./xkcd.
				imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
				for chunk in res.iter_content(100000):
					imageFile.write(chunk)
					imageFile.close()
			except ValueError: # todo figure out why this is happening
				print('Had trouble opening the file, so we were not able to write')

try:
	# Create and start the Thread objects.
	downloadThreads = [] # a list of all the Thread objects
	for i in range(0, 1400, 100): # loops 14 times, creates 14 threads
		downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
		downloadThreads.append(downloadThread)
		downloadThread.start()

	# Wait for all threads to end.
	for downloadThread in downloadThreads:
		downloadThread.join()
except (KeyboardInterrupt, SystemExit)
	print('\n\n KeyboardInterrupt received! We audi ')

print('Done.')