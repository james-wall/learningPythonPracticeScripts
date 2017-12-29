#! c:\Python36-32\python3.exe
# launches a map in the browser using an address from the command line or clipboard
# inspired by ATBSWP

import requests, bs4


# get user's current location.. TODO needs work on accuracy
freegeoip = "http://freegeoip.net/json"
geo_r = requests.get(freegeoip)
geo_json = geo_r.json()

res = requests.get('http://forecast.weather.gov/MapClick.php?lat='+ str(geo_json["latitude"]) + '&lon=' + str(geo_json["longitude"]))
res.raise_for_status()
exampleSoup = bs4.BeautifulSoup(res.text, "html.parser")
#print(exampleSoup.prettify())

elems = exampleSoup.find_all("p", class_="myforecast-current-lrg")
#elems = soup.select('span[id="myfcst-tempf"]')


if len(elems) < 1:
	print("no elements with this tag")
else:
	print('The temperature outside in ' + str(geo_json["city"]) + ', ' + str(geo_json["region_name"]) + ' (' + str(geo_json["country_name"]) + ') is ' + str(elems[0].getText()))