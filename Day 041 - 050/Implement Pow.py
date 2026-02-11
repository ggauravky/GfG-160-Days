# Implement Pow
# Difficulty: MediumAccuracy: 52.79%Submissions: 40K+Points: 4
# Implement the function power(b, e), which calculates b raised to the power of e (i.e. be).

# Examples:

# Input: b = 3.00000, e = 5
# Output: 243.00000
# Input: b = 0.55000, e = 3
# Output: 0.16638
# Input: b = -0.67000, e = -7
# Output: -16.49971

class Solution:
    def power(self, b: float, e: int) -> float:
        # Code Here
        return b**e