#! C:\Python36-32\python3.exe
# inspired by ATBSWP
# stopwatch.py - A simple stopwatch program.
import time
# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input() 		# press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)

		numHours = 0
		while totalTime > 3600:
			numHours = numHours + 1
			totalTime = totalTime - 3600

		numMinutes = 0
		while totalTime > 60:
			numMinutes = numMinutes + 1
			totalTime = totalTime - 60

		totalTime = round(totalTime, 2)
		print('Lap #%s: %s hours, %s minutes, %s seconds (%s seconds this lap)' % (lapNum, numHours, numMinutes, totalTime, lapTime), end='')
		lapNum += 1
		lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
	# Handle the Ctrl-C exception to keep its error message from displaying.
	print('\nDone.')