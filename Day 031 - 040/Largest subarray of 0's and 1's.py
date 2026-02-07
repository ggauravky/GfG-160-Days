# Largest subarray of 0's and 1's
# Difficulty: EasyAccuracy: 32.96%Submissions: 131K+Points: 2Average Time: 20m
# Given an array arr of 0s and 1s. Find and return the length of the longest subarray with equal number of 0s and 1s.

# Examples:

# Input: arr[] = [1, 0, 1, 1, 1, 0, 0]
# Output: 6
# Explanation: arr[1...6] is the longest subarray with three 0s and three 1s.
# Input: arr[] = [0, 0, 1, 1, 0]
# Output: 4
# Explnation: arr[0...3] or arr[1...4] is the longest subarray with two 0s and two 1s.
# Input: arr[] = [0]
# Output: 0
# Explnation: There is no subarray with an equal number of 0s and 1s.

class Solution:
    def maxLen(self, arr):
        prefix_sum = 0
        max_len = 0
        first_occurrence = {0: -1}

        for i in range(len(arr)):
            if arr[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum in first_occurrence:
                max_len = max(max_len, i - first_occurrence[prefix_sum])
            else:
                first_occurrence[prefix_sum] = i

        return max_len
