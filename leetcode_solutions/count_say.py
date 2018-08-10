'''
https://leetcode.com/problems/count-and-say/description/

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # if n == 1:
        #     return '1'
        num = '1'
        for i in range(n-1):
            num = self.create_str(num)
        return num

    def create_str(self, num):
        count = 1
        previous_num = num[0]
        string = ''
        for i in num[1:]:
            if i != previous_num:
                string = string + str(count) + previous_num
                previous_num = i
                count = 1
            else:
                count += 1
        if count != 0:
            string = string + str(count) + previous_num
        print(string)
        return string

sol=Solution()
print(sol.countAndSay(4))
