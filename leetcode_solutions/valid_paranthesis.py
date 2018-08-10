'''
https://leetcode.com/problems/valid-parentheses/description/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for brack in s:
            if brack == '(' or brack == '[' or brack == '{':
                stack.append(brack)
            else:
                br=''
                if stack:
                    br = stack.pop()
                if brack == ')' and br =='(':
                    continue
                elif brack == ']' and br =='[':
                    continue
                elif brack == '}' and br =='{':
                    continue
                else:
                    return False
        if not stack:
            return True
        return False
