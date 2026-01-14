# Maximum Product Subarray

# Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

# Note: It is guaranteed that the answer fits in a 32-bit integer.

# Examples

# Input: arr[] = [-2, 6, -3, -10, 0, 2]
# Output: 180
# Explanation: The subarray with maximum product is [6, -3, -10] with product = 6 * (-3) * (-10) = 180.
# Input: arr[] = [-1, -3, -10, 0, 6]
# Output: 30
# Explanation: The subarray with maximum product is [-3, -10] with product = (-3) * (-10) = 30.
# Input: arr[] = [2, 3, 4] 
# Output: 24 
# Explanation: For an array with all positive elements, the result is product of all elements. 

arr = [-2, 6, -3, -10, 0, 2]

def max_product_subarray(arr):
    if not arr:
        return 0

    max_so_far = arr[0]
    min_so_far = arr[0]
    result = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_so_far, min_so_far = min_so_far, max_so_far

        max_so_far = max(arr[i], max_so_far * arr[i])
        min_so_far = min(arr[i], min_so_far * arr[i])

        result = max(result, max_so_far)

    return result