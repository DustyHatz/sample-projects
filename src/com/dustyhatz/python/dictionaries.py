#-----------------------------------------------------------------#
# Having fun creating various functions to manipulate dictionaries
#-----------------------------------------------------------------#

# Takes in a dictionary
# Returns the sum of the values of the dictionary using a for loop
def sum_values(my_dictionary):

  sums = 0

  for value in my_dictionary.values():
    sums += value

  return sums
  

# Examples
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
print(sum_values({10:1, 100:2, 1000:3}))
# Print line break
print("-" * 40)


# Takes in a dictionary with all integer keys and values
# Returns the sum of the values of all even keys
def sum_even_keys(my_dictionary):

  sums = 0

  for key in my_dictionary:
      if key % 2 == 0:
        sums += my_dictionary[key]

  return sums
  

# Examples
print(sum_even_keys({1:5, 2:2, 3:3}))
print(sum_even_keys({10:1, 100:2, 1000:3}))
# Print line break
print("-" * 40)


# Takes in a dictionary with integer values
# Adds 10 to every value and returns the dictionary
def add_ten(my_dictionary):
  
  for key in my_dictionary:
    my_dictionary[key] += 10
    
  return my_dictionary
  

# Examples
print(add_ten({1:5, 2:2, 3:3}))
print(add_ten({10:1, 100:2, 1000:3}))
# Print line break
print("-" * 40)


# Takes in a dictionary
# Returns a list of all values in the dictionary that are also keys
def values_that_are_keys(my_dictionary):
  
  return [value for value in my_dictionary.values() if value in my_dictionary.keys()]
  
      
# Examples
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# Print line break
print("-" * 40)


# Takes in a dictionary
# Returns the key associated with the largest value in the dictionary
def max_key(my_dictionary):
  
  for key, value in my_dictionary.items():
    if value == max(my_dictionary.values()):
      return key
  

# Examples
print(max_key({1:100, 2:1, 3:4, 4:10}))
print(max_key({"a":100, "b":10, "c":1000}))
# Print line break
print("-" * 40)


# Takes in a list of strings
# Returns a dictionary where ever key is a word from the list and every value is the length of that word
def word_length_dictionary(words):
  
  return {word:len(word) for word in words}
  

# Examples
print(word_length_dictionary(["Dustin", "penny", "motorcycle"]))
print(word_length_dictionary(["a", ""]))
# Print line break
print("-" * 40)


# Takes in a list of elements
# Returns a dictionary containing the frequency of each element in the list
def frequency_dictionary(words):
  
  freq = {}
  
  for word in words:
    freq[word] = words.count(word)
  
  return freq
  
  
# Examples
print(frequency_dictionary(["Dustin", "Dustin", "dog", 1]))
print(frequency_dictionary([0,0,0,0,0]))
# Print line break
print("-" * 40)


# Takes in a dictionary
# Returns the number of unique values in the dictionary
def unique_values(my_dictionary):
  
  values = []
  
  for value in my_dictionary.values():
    if value not in values:
      values.append(value)
      
  return len(values)
  

# Examples
print(unique_values({0:3, 1:1, 4:1, 5:3}))
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# Print line break
print("-" * 40)


# Takes in a dictionary where the key is a last name and the value is a list of first names
# Returns a dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter
def count_first_letter(names):
  
  new_dict = {}
  
  for last_name in names.keys():
    if last_name[0] not in new_dict:
      new_dict[last_name[0]] = len(names[last_name])
      
    else:
      new_dict[last_name[0]] += len(names[last_name])
      
  return new_dict
  
  
# Examples
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# Print line break
print("-" * 40)



