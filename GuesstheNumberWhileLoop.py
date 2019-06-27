# imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing:print(aRandomNumber)

numberOfGuesses=0
while numberOfGuesses<3:
	guess = input("Guess a number between 1 and 20 (inclusive): ")
	numberOfGuesses+=1
	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
		print("That's not a positive whole number, try again!") #will have to rerun the code in order to try again.
	else:
		guess = int(guess) # converts a string to an integer

	if guess==aRandomNumber:
		print("Correct")
		break
	else:
		if numberOfGuesses>=3:
			print("The number was {}".format(aRandomNumber))
		elif guess<aRandomNumber:
			print("Guess higher")
		elif guess>aRandomNumber:
			print("Guess lower")
