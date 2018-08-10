'''
https://leetcode.com/problems/add-binary/description/

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

class Solution:
    def addBinary(self, a, b):
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        elif len(b) > len(a):
            a = '0' * (len(b) - len(a)) + a
        lim = len(a)-1
        result=''
        carry=0
        while lim>=0:
            result = str(int((int(a[lim]) + int(b[lim]) + carry)%2)) + result
            carry = int((int(a[lim]) + int(b[lim]) + carry)/2)
            lim-=1
        if carry == 1:
            result = str(carry) + result
        return result



sol = Solution()
print(sol.addBinary('11', '1'))
