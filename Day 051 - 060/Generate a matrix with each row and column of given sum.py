# Generate a matrix with each row and column of given sum
# Difficulty: EasyAccuracy: 82.52%Submissions: 2K+Points: 2
# Given two integer arrays rowSum[] of size n and colSum[] of size m, the task is to construct a 2D matrix of size n x m such that the sum of matrix elements in ith row is rowSum[i] and the sum of matrix elements in jth column is colSum[j].
# Note: Since multiple answers are possible, return any one of them. 
# Arrays are generated such that answer is always possible.
# The driver code will print true if output matrix is correct, otherwise it will print false.

# Examples:

# Input: rowSum[] = [5, 7, 10], colSum[] = [8, 6, 8]
# Output: true
# Explanation: For the matrix [[0, 5, 0], [6, 1, 0], [2, 0, 8]], we have row 1 with sum equal to 5 and column 1 has sum equal to 8.Row 2 has sum equal to 7 and column 2 has sum equal to 6.Row 3 has sum equal to 10 and column 3 has sum equal to 8.
# Input: rowSum[] = [1, 0], colSum[] = [1]
# Output: true
# Explanation: For the matrix [[1], [0]], we have row 1 with sum equal to 1 and column 1 has sum equal to 1.Row 2 with sum equal to 0.

class Solution:
    def generateMatrix(self, rowSum, colSum):
        n, m = len(rowSum), len(colSum)
        res = [[0] * m for _ in range(n)]
        
        i = j = 0
        
        while i < n and j < m:
            val = min(rowSum[i], colSum[j])
            res[i][j] = val
            
            rowSum[i] -= val
            colSum[j] -= val
            
            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1
        
        return res