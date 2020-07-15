# Example algorithm for performing a bubble sort


# Function for swapping two array elements with each other
def swap(arr, index_1, index_2):

	temp = arr[index_1]
	arr[index_1] = arr[index_2]
	arr[index_2] = temp


# Function to perform the bubble sort
def bubble_sort(arr):

	# Iterate through the indexes of the given array
	for i in range(len(arr)):

		# Iterate through unplaced elements
		for idx in range(len(arr) - i - 1):

			# If the current element is larger than the next then swap the elements with each other
			if arr[idx] > arr[idx + 1]:

				swap(arr, idx, idx + 1)


# Sample list of integers
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Print list before sort
print(f"Before Sort: {nums}")

# Perform the sort
bubble_sort(nums)

# Print the list after the sort
print(f"After Sort: {nums}")