# Set Matrix Zeros
# Difficulty: MediumAccuracy: 52.54%Submissions: 59K+Points: 4
# You are given a 2D matrix mat[][] of size n x m. The task is to modify the matrix such that if mat[i][j] is 0, all the elements in the i-th row and j-th column are set to 0.

# Examples:

# Input: 
    
# Output: 
    
# Explanation: mat[1][1] = 0, so all elements in row 1 and column 1 are updated to zeroes.
# Input: 
    
# Output: 
    
# Explanation: mat[0][0] and mat[0][3] are 0s, so all elements in row 0, column 0 and column 3 are updated to zeroes.

class Solution:
    def setMatrixZeroes(self, mat):   # <-- NOTE: Zeroes, not Zeros
        n = len(mat)
        m = len(mat[0])
        
        zero_rows = set()
        zero_cols = set()
        
        # Step 1: Find rows and columns containing 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        # Step 2: Update matrix
        for i in range(n):
            for j in range(m):
                if i in zero_rows or j in zero_cols:
                    mat[i][j] = 0
        
        return mat
