#! C:\Python36-34\python3.exe
# threadDemo.py - learning about threads (inspired by ATBSWP)

import threading, time
print('Start of program.')

def takeANap():
	time.sleep(5)
	print('Wake up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()
print('End of program.')