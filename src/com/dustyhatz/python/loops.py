#---------------------------------------------------------------#
# Having fun creating various loop functions to manipulate lists
#---------------------------------------------------------------#


# Takes in a list of numbers
# Returns the count of how many numbers in the list are divisable by 10
def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 == 0:
      count += 1
  return count
  

# Examples
print(divisible_by_ten([20, 25, 30, 35, 40]))
print(divisible_by_ten([20, 25, 100, 30, 35, 40, 110]))
# Print line break
print("-" * 40)


# Takes in a list of names
# Returns a list with the greeting "Hello, " before each name
def add_greetings(names):
  new_list = []
  
  for name in names:
    new_list.append(f"Hello, {name}")
  
  return new_list


# Examples
print(add_greetings(["Owen", "Max", "Sophie"]))
print(add_greetings(["Dustin", "Penny", "Cash", "Kalyn", "Mom"]))
# Print line break
print("-" * 40)


# Takes in a list of numbers
# Removes all numbers from the beginning of the list up to the first odd number
def delete_starting_evens(lst):
  while len(lst) > 0 and lst[0] % 2 == 0:
    lst = lst[1:]
  return lst
    

# Examples
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
# Print line break
print("-" * 40)


# Takes in a list of numbers
# Returns a new list of every element in the original list at an odd index
def odd_indices(lst):
  new_list = []
  for num in lst:
    if lst.index(num) % 2 != 0:
      new_list.append(num)
  return new_list

# Examples
print(odd_indices([4, 3, 7, 10, 11, -2]))
print(odd_indices([10, 4, 5]))
# Print line break
print("-" * 40)


# Takes in two separate lists of numbers
# Returns a new list of every number in the first list raised to the power of every number in the second list
def exponents(bases, powers):
  return [base ** power for base in bases for power in powers]

# Examples
print(exponents([2, 3, 4], [1, 2, 3]))
print(exponents([10, 5, 3], [2, 4, 6]))
# Print line break
print("-" * 40)


# Takes in two separate lists of numbers
# Returns the list with the highest sum of its elements. If sums are equal, returns list1
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  
  for num in lst1:
    sum1 += num
  for num in lst2:
    sum2 += num
  if sum1 >= sum2:
    return lst1
  return lst2
  
  
# Examples
print(larger_sum([1, 9, 5], [2, 3, 7]))
print(larger_sum([65, 3, 56, 36], [22, 90, 7]))
# Print line break
print("-" * 40)


# Takes in a list
# Adds all elements of the list until the sum is greater than 9000
# When this happens it returns the sum
# If the sum is never greater than 9000 it returns the sum of all elements
# If the list is empty it returns 0
def over_nine_thousand(lst):
  sum = 0
  
  if len(lst) > 0:
    for num in lst:
      if sum <= 9000:
        sum += num
    return sum
  return 0
  

# Examples
print(over_nine_thousand([8000, 900, 120, 5000]))
print(over_nine_thousand([1, 2, 3, 4]))
print(over_nine_thousand([]))
# Print line break
print("-" * 40)


# Takes in a list of numbers
# Returns the largest number in the list using a loop rather than sorting

def max_num(nums):
  a = nums[0]
  for num in nums[1:]:
    if num > a: 
      a = num
  return a  


# Examples
print(max_num([50, -10, 0, 75, 20]))
print(max_num([78, 32, 10, 3, 46]))
# Print line break
print("-" * 40)


# Takes in two separate lists of numbers
# Returns a list of the indices where values are equal from lst1 and lst2
def same_values(lst1, lst2):
  if len(lst1) < len(lst2):
    return [i for i in range(len(lst1)) if lst1[i] == lst2[i]]
  
  return [i for i in range(len(lst2)) if lst1[i] == lst2[i]]
  

# Examples
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
print(same_values([5, 1, -10, 3, 3, 2, 30, 1, 23], [5, 10, -10, 3, 5, 2, 10, 23, 23, 30]))
# Print line break
print("-" * 40)


# Takes in two separate lists of the same size
# Returns True if lst1 is the same size as lst2, otherwise returns False
def reversed_list(lst1, lst2):
  if len(lst1) == len(lst2):
    lst2_rev = []
    
    # Reverse lst2
    for i in lst2[::-1]:
      lst2_rev.append(i)
      
    if lst1 == lst2_rev:
      return True
    return False
  
  return 0
    

# Examples
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
# Print line break
print("-" * 40)

