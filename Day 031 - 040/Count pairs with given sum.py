# Count pairs with given sum
# Prev
# Next
# Difficulty: MediumAccuracy: 50.11%Submissions: 61K+Points: 4Average Time: 15m
# You are given an array arr[] and an integer target. You have to count all pairs in the array such that their sum is equal to the given target.

# Examples:

# Input: arr[] = [1, 5, 7, -1, 5], target = 6 
# Output: 3
# Explanation: Pairs with sum 6 are (1, 5), (7, -1) and (1, 5). 
# Input: arr[] = [1, 1, 1, 1], target = 2 
# Output: 6
# Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1).
# Input: arr[] = [10, 12, 10, 15, -1], target = 125
# Output: 0
# Explanation: There is no pair with sum = target

class Solution:
    def countPairs(self, arr, target):
        count = 0
        freq = {}
        
        for num in arr:
            complement = target - num
            if complement in freq:
                count += freq[complement]
            
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        return count