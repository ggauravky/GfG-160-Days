# Sum Pair closest to target
# Difficulty: EasyAccuracy: 44.75%Submissions: 73K+Points: 2
# Given an array arr[] and a number target, find a pair of elements (a, b) in arr[], where a ≤ b whose sum is closest to target.
# Note: Return the pair in sorted order and if there are multiple such pairs return the pair with maximum absolute difference. If no such pair exists return an empty array.

# Examples:

# Input: arr[] = [10, 30, 20, 5], target = 25
# Output: [5, 20]
# Explanation: As 5 + 20 = 25 is closest to 25.
# Input: arr[] = [5, 2, 7, 1, 4], target = 10
# Output: [2, 7]
# Explanation: As (4, 5), (2, 7) and (4, 7) both are closest to 10, but absolute difference of (4, 5) is 1, (2, 7) is 5 and (4, 7) is 3. Hence, [2, 7] has maximum absolute difference and closest to target. 
# Input: arr[] = [10], target = 10
# Output: []
# Explanation: As the input array has only 1 element, return an empty array.

class Solution:
    def sumClosest(self, arr, target):
        arr.sort()
        left, right = 0, len(arr) - 1
        closest_pair = []
        min_diff = float('inf')

        while left < right:
            current_sum = arr[left] + arr[right]
            current_diff = abs(target - current_sum)

            if current_diff < min_diff or (current_diff == min_diff and (not closest_pair or abs(arr[left] - arr[right]) > abs(closest_pair[0] - closest_pair[1]))):
                min_diff = current_diff
                closest_pair = [arr[left], arr[right]]

            if current_sum < target:
                left += 1
            else:
                right -= 1

        return closest_pair