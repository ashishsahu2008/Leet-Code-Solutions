'''
https://leetcode.com/problems/hamming-distance/description/

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = format(x, 'b')
        bin_y = format(y, 'b')
        max_len = len(bin_x) if len(bin_x) > len(bin_y) else len(bin_y)
        bin_x = bin_x.zfill(max_len)
        bin_y = bin_y.zfill(max_len)
        total = 0
        for i,j in zip(range(len(bin_x)), range(len(bin_y))):
            if bin_x[i] != bin_y[j]:
                total +=1
        return total

    def best_solution(self, x, y):
        return str(bin(x ^ y))[2:].count('1')

sol = Solution()
print(sol.hammingDistance(1,4))
