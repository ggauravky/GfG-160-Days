# Search in Rotated Sorted Array
# Difficulty: MediumAccuracy: 37.64%Submissions: 292K+Points: 4
# Given an array arr[] of distinct elements, which was initially sorted in ascending order but then rotated at some unknown pivot, the task is to find the index of a target key.  If the key is not present in the array, return -1.

# Examples :

# Input: arr[] = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 3
# Output: 8
# Explanation: 3 is found at index 8.
# Input: arr[] = [3, 5, 1, 2], key = 6
# Output: -1
# Explanation: There is no element that has value 6.
# Input: arr[] = [33, 42, 72, 99], key = 42
# Output: 1
# Explanation: 42 is found at index 1.

class Solution:
    def search(self, arr, key):
        # code here
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == key:
                return mid
            if arr[left] <= arr[mid]:  
                if arr[left] <= key < arr[mid]:
                    right = mid + 1
                else:
                    left = mid - 1
            else:  
                if arr[mid] < key <= arr[right]:
                    left = mid - 1
                else:
                    right = mid - 1
        return -1
    
    # wrong approach