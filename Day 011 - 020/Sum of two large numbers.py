# Sum of two large numbers

# Given two strings denoting non-negative numbers s1 and s2. Calculate the sum of s1 and s2.

# Examples:

# Input: s1 = "25", s2 = "23"
# Output: "48"
# Explanation: The sum of 25 and 23 is 48.
# Input: s1 = "2500", s2 = "23"
# Output: "2523"
# Explanation: The sum of 2500 and 23 is 2523.
# Input: s1 = "2", s2 = "3"
# Output: "5"
# Explanation: The sum of 2 and 3 is 5.

class Solution:
    def findSum(self, s1, s2):
        # reverse both strings
        s1 = s1[::-1]
        s2 = s2[::-1]

        i = 0
        carry = 0
        ans = []

        # add digits
        while i < len(s1) or i < len(s2) or carry:
            d1 = int(s1[i]) if i < len(s1) else 0
            d2 = int(s2[i]) if i < len(s2) else 0

            total = d1 + d2 + carry
            ans.append(str(total % 10))
            carry = total // 10

            i += 1

        result =''.join(ans[::-1])
        
        result=result.lstrip('0')
        
        return result if result else '0'
