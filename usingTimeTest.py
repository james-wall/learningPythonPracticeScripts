#! C:\Python36-32\python3.exe
# inspired by ATBSWP

import time
def calcProd():
	# Calculate the product of the first 100,000 numbers.
	product = 1
	for i in range(1, 100000):
		product = product * i
	return product

print('Starting...')
startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))