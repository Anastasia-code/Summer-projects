import random

# A list of random words to guess later
potential_words = ["computer", "program", "frame", "python", "programmer"]

word = random.choice(potential_words)  #random word chosen

# Use to test your code: print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = []
for i in word:
	current_word.extend(["_"])    #prints the amount of spaces in the secret word
print(current_word)

#some useful variables
guesses = []  #stores the letters guessed
maxfails = 7
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")

	# check if the guess is valid: Have they already guessed it? Is it a letter? Is it one letter?
	if guess in guesses:
		print("Already guessed")
		continue #restarts the while loop

	if not guess.isalpha(): #checks if it's a letter
		print("Not a letter.")
		continue

	if len(guess)>1:
		print("Invalid guess.")
		continue

	guesses.append(guess)  #appends guessed letter to list of guessed letters
	# check if the guess is correct: If it's in the word then "_" changed to guess.
	for i in range(len(word)):
		if guess==word[i]:
			current_word[i]=guess  #Another way but only can change one underscore at a time: current_word[word.index(guess)]=guess

	print(current_word)

	if "_" not in current_word:
		print("Congratulations you guessed the word!")
		break

	if "_" in current_word:
		inputed_guess=input("Write your full guess of the word:")
		if inputed_guess==word:
			print("Congratulations you guessed the word!")
			break
		else:
			print("Incorrect.")

	fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")

	if fails>=maxfails:
		print("Game Over. The word was " + word)
