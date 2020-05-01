#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    #Calculate diagonal sums
    sum_L = 0
    sum_R = 0

    #Left diagonal pointer begins at 0th index
    i = 0

    #Right diagonal pointer begins at -1th index
    j = -1

    for row in arr:
        sum_L += row[i]
        i += 1
        sum_R += row[j]
        j -= 1

    #Return the absolute difference between the diagonal sums
    return abs(sum_L - sum_R)


arr =   [[1,2,3,4,5,6,7]
    	,[6,3,7,4,8,9,2]
    	,[5,2,7,4,6,9,4]
    	,[8,9,3,5,5,8,4]
    	,[8,9,0,4,2,6,8]
    	,[9,9,5,2,8,1,6]
    	,[6,8,3,5,7,2,8]]

arr_2 = [[4,5,6]
				,[7,8,9]
				,[1,2,0]]

print(diagonalDifference(arr))
print(diagonalDifference(arr_2))

