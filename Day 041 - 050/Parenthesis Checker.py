# Parenthesis Checker
# Difficulty: EasyAccuracy: 28.56%Submissions: 722K+Points: 2
# Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']'. Determine whether the Expression is balanced or not.
# An expression is balanced if:

# Each opening bracket has a corresponding closing bracket of the same type.
# Opening brackets must be closed in the correct order.
# Examples :

# Input: s = "[{()}]"
# Output: true
# Explanation: All the brackets are well-formed.
# Input: s = "[()()]{}"
# Output: true
# Explanation: All the brackets are well-formed.
# Input: s = "([]"
# Output: false
# Explanation: The expression is not balanced as there is a missing ')' at the end.
# Input: s = "([{]})"
# Output: false
# Explanation: The expression is not balanced as there is a closing ']' before the closing '}'.

class Solution:
    def isBalanced(self, s):
        # code here
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack