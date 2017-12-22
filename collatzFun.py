def collatz(number):
	if number % 2 == 0:
		return number // 2
	else:
		return 3 * number + 1;

def goToOneUsingCollatz():
	number = None
	while(number == None):
		try:
			number = int(input("Give us a number please: "))
		except (ValueError, TypeError) as exception:
			print("Invalid input type, make sure you input an integer")

	print('The number that you inputted is: ' + str(number))
	iteration = 0
	while(number != 1):
		number = collatz(number)
		iteration = iteration + 1
		print("collatz number " + str(iteration) + " gives us the value: " + str(number))
	print("Awesome! We got to one in " + str(iteration) + " iterations of collatz.")


goToOneUsingCollatz()
