#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)

for numberOfGames in range(3):
	guess = input("Guess a number between 1 and 20 (inclusive): ")
	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
		print("That's not a positive whole number, try again!")
	else:
		guess = int(guess) # converts a string to an integer

	if guess==aRandomNumber:
		print("Correct")
		break
	else:
		if numberOfGames==2:  #if that was their last guess, then prints wat answer is.
			print("The number was {}".format(aRandomNumber))
			break
		elif guess<aRandomNumber:
			print("Guess higher")
		elif guess>aRandomNumber:
			print("Guess lower")
