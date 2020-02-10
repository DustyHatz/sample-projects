# Function that returns the character that is the first occurence of a non repeating character in a given string
# Given string consists of all lowercase english letters

def non_repeating(string):
	char_counts = {}
	for char in string:
		char_counts.update({char : string.count(char)})
	
	for char in string:
		if char_counts[char] == 1:
			return char

print(non_repeating("aaaaabbccdeeeeedefkkkkloofoijskklll"))