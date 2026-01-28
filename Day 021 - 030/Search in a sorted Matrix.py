# Search in a sorted Matrix
# Difficulty: MediumAccuracy: 56.27%Submissions: 151K+Points: 4
# Given a strictly sorted 2D matrix mat[][] of size n x m and a number x. Find whether the number x is present in the matrix or not.
# Note: In a strictly sorted matrix, each row is sorted in strictly increasing order, and the first element of the ith row (i!=0) is greater than the last element of the (i-1)th row.

# Examples:

# Input: mat[][] = [[1, 5, 9], [14, 20, 21], [30, 34, 43]], x = 14
# Output: true
# Explanation: 14 is present in the matrix, so output is true.
# Input: mat[][] = [[1, 5, 9, 11], [14, 20, 21, 26], [30, 34, 43, 50]], x = 42
# Output: false
# Explanation: 42 is not present in the matrix.
# Input: mat[][] = [[87, 96, 99], [101, 103, 111]], x = 101
# Output: true
# Explanation: 101 is present in the matrix.


class Solution:
    def searchMatrix(self, mat, x):
        n = len(mat)
        m = len(mat[0]) if n > 0 else 0

        left, right = 0, n * m - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_value = mat[mid // m][mid % m]

            if mid_value == x:
                return True
            elif mid_value < x:
                left = mid + 1
            else:
                right = mid - 1

        return False