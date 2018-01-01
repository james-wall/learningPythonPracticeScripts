#! C:\Python36-32\python3.exe
# isItChristmasYet.py - to check if its Christmas yet

import datetime, time

now = datetime.datetime.now()

def getNumberOfDaysUntilNextChristmas():
	print('Alas, tis not Christmas')
	futureChristmasYear = now.year + 1 if now.month == 12 and now.day > 25 else now.year
	futureChristmas = datetime.date(futureChristmasYear, 12, 25)
	today = datetime.date.today()
	diff = futureChristmas - today
	print('Only ' + str(diff.days) + ' days until Christmas!')

if now.month == 12:
	if now.day == 25:
		print('YES!! It is Christmas')
	elif now.day == 24:
		print('Almost! It is Christmas Eve')
	else:		
		getNumberOfDaysUntilNextChristmas()
else:
	getNumberOfDaysUntilNextChristmas()
