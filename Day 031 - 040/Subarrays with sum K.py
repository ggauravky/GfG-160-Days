# Subarrays with sum K
# Difficulty: MediumAccuracy: 49.74%Submissions: 102K+Points: 4
# Given an unsorted array arr[] of integers, find the number of subarrays whose sum exactly equal to a given number k.

# Examples:

# Input: arr[] = [10, 2, -2, -20, 10], k = -10
# Output: 3
# Explaination: Subarrays: arr[0...3], arr[1...4], arr[3...4] have sum exactly equal to -10.
# Input: arr[] = [9, 4, 20, 3, 10, 5], k = 33
# Output: 2
# Explaination: Subarrays: arr[0...2], arr[2...4] have sum exactly equal to 33.
# Input: arr[] = [1, 3, 5], k = 0
# Output: 0
# Explaination: No subarray with 0 sum.

class Solution:
    def cntSubarrays(self, arr, k):
        prefix_count = {0: 1}   # prefix sum frequency map
        current_sum = 0
        count = 0

        for num in arr:
            current_sum += num

            # Check if (current_sum - k) exists
            if current_sum - k in prefix_count:
                count += prefix_count[current_sum - k]

            # Store current prefix sum
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        return count
