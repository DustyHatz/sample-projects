#### Guess a number between 1 and 10! ####

from random import randint


# Get user input and ensure it is an integer between 1 and 10 inclusive
def inputNum(message):

	while True:
		try:
			userInput = int(input(message))

		except ValueError:
			print("Must enter an integer!")
			continue

		if userInput < 1 or userInput > 10:
			print("Must enter a number between 1 and 10!")
			continue

		else:
			return userInput
			break


# Compare the user's guess with the random chosen number
def compareNums(guess, chosenNum):

	if guess < chosenNum:
		print("Your guess is lower than the chosen number...")
		guess = inputNum("Guess again: ")
		return compareNums(guess, chosenNum)

	if guess > chosenNum:
		print("Your guess is higher than the chosen number...")
		guess = inputNum("Guess again: ")
		return compareNums(guess, chosenNum)

	else:
		print(f"Your guess was {guess} and the chosen number was {chosenNum}! YOU WIN!")
		return 1


# Get the user's guess
guess = inputNum("Guess a number between 1 and 10: ")

# Generate a random integer between 1 and 10 inclusive
chosenNum = randint(1, 10)

# Compare the numbers and get the result!
compareNums(guess, chosenNum)