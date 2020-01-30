# Basic framework for a 'Magic 8 Ball' question and response game #


import random


# Dict of possible Magic 8 Ball responses
responses = {1 : "Absolutely!", 2 : "Maybe.", 3 : "Ask again later.", 
4 : "Better not tell you now.", 5 : "Don’t count on it.", 6 : "It is certain.", 
7 : "Most likely.", 8 : "My sources say no.", 9 : "Signs point to yes.", 
10 : "Very doubtful.", 11 : "Without a doubt.", 12 : "You may rely on it.", 
13 : "Concentrate and ask again.", 14 : "Maybe, but probably not.", 
15 : "I don't understand the question and I won't responde to it."
}


# Function to ask a question and print a response
def ask_magic_8_ball():

	question = input("Ask a question: ")

	if question[-1] == "?":

		response = responses.get(random.randint(1, 15))

		print(response)

	else:
		print('Must enter a yes or no question that ends with "?"')
		ask_question()


# Ask question
ask_magic_8_ball()