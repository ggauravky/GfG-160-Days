#  Pair with given sum in a sorted array
# Difficulty: EasyAccuracy: 26.04%Submissions: 107K+Points: 2
# You are given an integer target and an array arr[]. You have to find number of pairs in arr[] which sums up to target. It is given that the elements of the arr[] are in sorted order.
# Note: pairs should have elements of distinct indexes. 

# Examples :

# Input: arr[] = [-1, 1, 5, 5, 7], target = 6
# Output: 3
# Explanation: There are 3 pairs which sum up to 6 : {1, 5}, {1, 5} and {-1, 7}.
# Input: arr[] = [1, 1, 1, 1], target = 2
# Output: 6
# Explanation: There are 6 pairs which sum up to 2 : {1, 1}, {1, 1}, {1, 1}, {1, 1}, {1, 1} and {1, 1}.
# Input: arr[] = [-1, 10, 10, 12, 15], target = 125
# Output: 0
# Explanation: There is no such pair which sums up to 125.


class Solution:
    def countPairs(self, arr, target):
        left = 0
        right = len(arr) - 1
        count = 0

        while left < right:
            s = arr[left] + arr[right]

            # Case 1: Sum found
            if s == target:

                # If both values are same
                if arr[left] == arr[right]:
                    n = right - left + 1
                    count += (n * (n - 1)) // 2
                    break

                # Count duplicates on left side
                left_val = arr[left]
                left_count = 0
                while left <= right and arr[left] == left_val:
                    left_count += 1
                    left += 1

                # Count duplicates on right side
                right_val = arr[right]
                right_count = 0
                while right >= left and arr[right] == right_val:
                    right_count += 1
                    right -= 1

                count += left_count * right_count

            # Case 2: Sum too small → move left
            elif s < target:
                left += 1

            # Case 3: Sum too big → move right
            else:
                right -= 1

        return count
