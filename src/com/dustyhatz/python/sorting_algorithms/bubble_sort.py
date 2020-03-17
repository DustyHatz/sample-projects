def swap(arr, index_1, index_2):
  temp = arr[index_1]
  arr[index_1] = arr[index_2]
  arr[index_2] = temp


def bubble_sort(arr):
  iteration_count = 0
  for i in range(len(arr)):
    # iterate through unplaced elements
    for idx in range(len(arr) - i - 1):
      iteration_count += 1
      if arr[idx] > arr[idx + 1]:
        swap(arr, idx, idx + 1)


nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(f"Before Sort: {nums}")

bubble_sort(nums)

print(f"After Sort: {nums}")