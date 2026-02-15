# Implement Lower Bound
# Difficulty: EasyAccuracy: 50.04%Submissions: 74K+Points: 2
# Given a sorted array arr[] and a number target, the task is to find the lower bound of the target in this given array. The lower bound of a number is defined as the smallest index in the sorted array where the element is greater than or equal to the given number.

# Note: If all the elements in the given array are smaller than the target, the lower bound will be the length of the array. 

# Examples :

# Input:  arr[] = [2, 3, 7, 10, 11, 11, 25], target = 9
# Output: 3
# Explanation: 3 is the smallest index in arr[] where element (arr[3] = 10) is greater than or equal to 9.
# Input: arr[] = [2, 3, 7, 10, 11, 11, 25], target = 11
# Output: 4
# Explanation: 4 is the smallest index in arr[] where element (arr[4] = 11) is greater than or equal to 11.
# Input: arr[] = [2, 3, 7, 10, 11, 11, 25], target = 100
# Output: 7
# Explanation: As no element in arr[] is greater than 100, return the length of array.


arr= [2, 3, 7, 10, 11, 11, 25]
target = 11

for i in range(len(arr)):
    if arr[i]>=target:
        print(i)
        break
    if max(arr)<=target:
        print(len(arr))
        break
    
    
class Solution:
    def lowerBound(self, arr, target):
        low = 0
        high = len(arr) - 1
        ans = len(arr)  # default if not found

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] >= target:
                ans = mid
                high = mid - 1  # search left part
            else:
                low = mid + 1   # search right part

        return ans