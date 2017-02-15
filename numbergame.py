
from random import randint
answer = "yes"
while answer == "yes": 


	random_number = randint(0, 100)
	number_tries = 0
	num = - 5

	while num != random_number:
		num = int(raw_input("Please pick a number 1 to 100. "))
		number_tries = number_tries + 1
		if num < random_number:
			print "Your number is too low. "
		elif num > random_number:
			print "Your number is too high. "
		else:
			print "You picked the correct number! " 
			print "It took you", number_tries, "tries !"
		

	answer = str(raw_input("Would you like to play again? ")).lower


# limit number of tries, best of three rounds, keep some statitics 