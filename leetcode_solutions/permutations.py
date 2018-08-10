'''
https://leetcode.com/problems/permutations/description/
https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
'''
class Solution:
    def permutation(self, nums):
        list=[]
        self.backtrack(list, [], nums)
        return list

    def backtrack(self, list, temp, nums):
        if len(temp) == len(nums):
            list.append(temp[:len(temp)])
        for i in range(len(nums)):
            if nums[i] in temp:
                continue
            temp.append(nums[i])
            self.backtrack(list, temp, nums)
            del temp[len(temp)-1]

sol = Solution()
print(sol.permutation([1,2,3]))
