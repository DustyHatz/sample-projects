#--------------------------------------------------------------#
# Having fun creating various functions to manipulate strings
#--------------------------------------------------------------#

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Takes in a string (word)
# Returns the total number of unique letters in the string using the provided string 'letters'
# Uppercase and lowercase letters are counted as different letters
def unique_english_letters(word):
  total_letters = 0
  for letter in letters:
    if letter in word:
      total_letters += 1

  return total_letters
      

# Examples
print(unique_english_letters("Dustin"))
print(unique_english_letters("Hatzenbuhler"))
# Print line break
print("-" * 40)


# Takes in a string and a single character
# Returns the number of times the character appears in the string
def count_char_x(word, x):
    count = [x for letter in word if letter == x]
    return len(count)
  
# Examples
print(count_char_x("mississippi", "s"))
print(count_char_x("tomorrow", "o"))
# Print line break
print("-" * 40)


# Takes in two separate strings
# Returns the number of times the second string appears in the first string
def count_multi_char_x(word, x):
  if x in word:
    split = word.split(x)

  return len(split) - 1
  
# Examples
print(count_multi_char_x("mississippi", "iss"))
print(count_multi_char_x("apple", "pp"))
# Print line break
print("-" * 40)

# Takes in a string, a single character to start at, and a single character to end at.
# Returns the substring between the first occurence of the starting and ending characters in the string.
# If the starting or ending characters are not in the string, returns the string 
def substring_between_letters(word, start, end):
  if start in word and end in word:
    slice1 = word.find(start) + 1

    if slice1 == 0:
      return word

    slice2 = word[slice1:].find(end)

    if slice2 == -1:
      return word
    return word[slice1 : slice2 + slice1]
  return word
    
  
# Examples
print(substring_between_letters("apple", "p", "e"))
print(substring_between_letters("mississippi", "i", "i"))
# Print line break
print("-" * 40)


# Takes in a string and an integer
# Returns True if every word in the string has a length greater than or equal to the integer
def x_length_words(sentence, x):
  sentence_split = sentence.split()
  for word in sentence_split:
    if len(word) >= x:
      return True

    return False
    

# Examples
print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))
# Print line break
print("-" * 40)


# Takes in two separate strings: a sentence and a name
# Returns True if the name appears in the sentence, otherwise returns False
def check_for_name(sentence, name):
  if name.casefold() in sentence.casefold():
    return True
  
  return False
  
# Examples
print(check_for_name("My name is Dustin", "Dustin"))
print(check_for_name("My name is dustin", "Dustin"))
print(check_for_name("My name is Samantha", "Dustin"))
# Print line break
print("-" * 40)


# Takes in a string
# Returns a string containing every other letter in word
def every_other_letter(word):
  letters = list(word)
  letters_sliced = letters[::2]
  return "".join(letters_sliced)  
  
# Examples
print(every_other_letter("Dustin"))
print(every_other_letter("Hello world!"))
# Print line break
print("-" * 40)


# Takes in a string
# Returns the string in reverse
def reverse_string(word):
  word_reversed = [letter for letter in word[::-1]]
  return "".join(word_reversed)

# Examples
print(reverse_string("Dustin"))
print(reverse_string("Hello world!"))
# Print line break
print("-" * 40)


# Takes in two strings
# Returns a string with the first letter in word1 and word2 swapped
def make_spoonerism(word1, word2):
  word1_spoon = word1.replace(word1[0], word2[0])
  word2_spoon = word2.replace(word2[0], word1[0])
  return f"{word1_spoon} {word2_spoon}"
  
# Example
print(make_spoonerism("Dustin", "Hatzenbuhler"))
print(make_spoonerism("Hello", "world!"))
print(make_spoonerism("a", "b"))
# Print line break
print("-" * 40)


# Takes in a string
# Returns the string with added exclamation points until the string is 20 characters long
# If the string is already at least 20 characters long it returns the string
def add_exclamation(word):
  if len(word) < 20:
    return word + "!" * (20 - len(word))
  
  return word
  
# Examples
print(add_exclamation("Dustin"))
print(add_exclamation("Dustin Hatzenbuhler"))
# Print line break
print("-" * 40)



