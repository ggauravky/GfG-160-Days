# Roman to Integer
# Difficulty: EasyAccuracy: 43.31%Submissions: 211K+Points: 2Average Time: 20m
# Given a string s in Roman number format, your task is to convert it to an integer. Various symbols and their values are given below.
# Note: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

# Examples:

# Input: s = "IX"
# Output: 9
# Explanation: IX is a Roman symbol which represents 10 – 1 = 9.
# Input: s = "XL"
# Output: 40
# Explanation: XL is a Roman symbol which represents 50 – 10 = 40.
# Input: s = "MCMIV"
# Output: 1904
# Explanation: M is 1000, CM is 1000 – 100 = 900, and IV is 4. So we have total as 1000 + 900 + 4 = 1904.

class Solution:
    def romanToDecimal(self, s): 
        # code here
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        num = 0
        while i < len(s):
            if i+1<len(s) and s[i:i+2] in roman:
                num+=roman[s[i:i+2]]
                i+=2
            else:
                num+=roman[s[i]]
                i+=1
        return num