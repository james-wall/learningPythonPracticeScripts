#! c:\Python36-32\python3.exe
# launches a map in the browser using an address from the command line or clipboard
# inspired by ATBSWP

import requests, bs4

res = requests.get('http://forecast.weather.gov/MapClick.php?lat=42.320364900000015&lon=-71.2566061')
res.raise_for_status()
exampleSoup = bs4.BeautifulSoup(res.text, "html.parser")
#print(exampleSoup.prettify())

elems = exampleSoup.find_all("p", class_="myforecast-current-lrg")
#elems = soup.select('span[id="myfcst-tempf"]')


if len(elems) < 1:
	print("no elements with this tag")
else:
	print(str(elems[0].getText()))