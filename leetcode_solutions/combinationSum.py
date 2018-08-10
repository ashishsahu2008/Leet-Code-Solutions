'''
https://leetcode.com/problems/combination-sum/description/
https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
'''
class Solution:
    def combination_sum(self, candidates, target):
        list=[]
        self.backtrack(list, [], candidates, target, 0)
        return list

    def backtrack(self, list, temp, candidates, remain, start):
        if remain == 0:
            list.append(temp[:len(temp)])
        for i in range(start, len(candidates)):
            if remain - candidates[i]>=0:
                temp.append(candidates[i])
                self.backtrack(list, temp, candidates, remain-candidates[i], i)
                del temp[len(temp)-1]

sol = Solution()
print(sol.combination_sum([2,3,6,7], 7))
