# Rotate Array

# Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

# Note: Consider the array as circular.

# Examples :

# Input: arr[] = [1, 2, 3, 4, 5], d = 2
# Output: [3, 4, 5, 1, 2]
# Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.
# Input: arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3
# Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]
# Explanation: when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.
# Input: arr[] = [7, 3, 9, 1], d = 9
# Output: [3, 9, 1, 7]
# Explanation: when we rotate 9 times, we'll get 3 9 1 7 as resultant array.

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
d = 3

for i in range(d):
    # print(i)
    removed_item = arr.pop(0)
    # print(removed_item)
    arr.append(removed_item)

# print(arr)

# more expensive


def rotateArr(arr, d):
    n = len(arr)
    d = d % n

    result = [0] * n
    i = 0

    for j in range(d, n):
        result[i] = arr[j]
        i += 1

    for j in range(d):
        result[i] = arr[j]
        i += 1

    arr[:] = result
