#--------------------------------------------------------------#
# Having fun creating various functions to manipulate lists
#--------------------------------------------------------------#


# Takes in a list and a single number as index
# Returns a new list identical to the original except the value at specified index is doubled.
def double_index(lst, index):
  try:
    lst[index] = lst[index] * 2
    return lst
  
  except IndexError:
    return lst
  
# Examples
print(double_index([3, 8, -10, 12], 2))
print(double_index([5, 30, 26, 1, 45, 3], 4))
# Print line break
print("-" * 40)


# Takes in a list, a starting index, and an ending index
# Returns the original list with elements between start and end (inclusive) removed
def remove_middle(lst, start, end):
  try:
    first_half = lst[:start]
    second_half = lst[end + 1:]
    return first_half + second_half
  
  except IndexError:
    return lst

#Uncomment the line below when your function is done
print(remove_middle([4, -8, 15, 16, 23, 42], 1, 2))
print(remove_middle([8, 37, -2, 19, 6, 90, 36], 3, 6))
# Print line break
print("-" * 40)


# Takes in a list, a list element, and a counter
# Returns true if the list element appears in the the list more than n times, otherwise returns false
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  
  return False

# Examples
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 1, 1))
# Print line break
print("-" * 40)


# Takes in a list, and two separate list elements
# Returns the list element that appears more often than the other
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) > lst.count(item2):
    return item1
  
  elif lst.count(item1) < lst.count(item2):
    return item2
  
  else:
    return item1
  
# Examples
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
print(more_frequent_item(["mom", "dad", "mom", "sister", "mom", "brother", "dad", "sister"], "mom", "dad"))
# Print line break
print("-" * 40)


# Takes in a list
# Returns the middle element if number of elements is odd, otherwise returns the average of the two middle elements
def middle_element(lst):
  
  if len(lst) % 2 != 0:
    middle = int(len(lst)/2)
    return lst[middle]
  
  else:
    middle = int(len(lst) / 2)
    middle2 = int(len(lst) / 2) - 1
    return (lst[middle] + lst[middle2]) / 2

# Examples
print(middle_element([5, 2, -10, 48, 4, 5]))
print(middle_element([5, 2, -10, -4, 48, 5, 7]))
# Print line break
print("-" * 40)


# Takes in a list
# Appends to the list the sum of the last two elements in the list (three times)
def append_sum(lst):
  for i in range(3):
    lst.append(lst[-1] + lst[-2])
  return lst

# Exmaples
print(append_sum([1, 1, 2]))
print(append_sum([43, 21, 60]))
# Print line break
print("-" * 40)


# Takes in two separate lists
# Returns the last element of the list that contains the most elements. If lists are equal length, returns last element of lst1
def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]

# Examples
print(larger_list([2, 5], [-10, 2, 5, 10]))
print(larger_list([2, 5, 9, 20], [-10, 2, 5, 10]))
# Print line break
print("-" * 40)


# Takes in two separate lists
# Combines two separate lists into a new sorted list
def combine_sort(lst1, lst2):
  return sorted(lst1 + lst2)

# Examples
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
print(combine_sort([6, 29, 1, 68], [-17, 32, 0, 23]))
# Print line break
print("-" * 40)


# Takes in a list
# Appends the size of the list to the end of the list
def append_size(lst):
  lst.append(len(lst))
  return lst

# Examples
print(append_size([23, 42, 108]))
print(append_size([23, 42, 108, 42, 108, 42, 108]))
# Print line break
print("-" * 40)


# Returns a list of every third number between start and 100 (inclusive)
# If start is greater than 100 it returns an empty list
def every_three_nums(start):
  if start < 100:
    return list(range(start, 101, 3))
  else:
    return []

# Examples
print(every_three_nums(91))
print(every_three_nums(101))
# Print line break
print("-" * 40)

