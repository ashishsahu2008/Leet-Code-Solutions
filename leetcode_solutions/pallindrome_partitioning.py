'''
https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
https://leetcode.com/problems/palindrome-partitioning/description/
'''
class Solution:
    def pallindrome_partitioning(self, s):
        list=[]
        self.backtrack(list, [], s, 0)
        return list

    def backtrack(self, list, temp, s, start):
        if start == len(s):
            list.append(temp[:len(temp)])
        for i in range(start, len(s)):
            if self.isPallindrome(s, start, i) :
                temp.append(s[start:i+1])
                self.backtrack(list, temp, s, i+1)
                del temp[len(temp)-1]

    def isPallindrome(self, s, start, i):
        while start == i:
            if s[start] != s[i]:
                return False
            start+=1
            i-=1
        return True

sol = Solution()
print(sol.pallindrome_partitioning('aab'))
