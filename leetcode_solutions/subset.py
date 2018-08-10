'''
https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
https://leetcode.com/problems/subsets/description/
'''
class Solution:
    def subset(self, nums):
        list = []
        self.backtrack(list, [], nums, 0)
        return list

    def backtrack(self, list, temp, nums, start):
        list.append(temp[:len(temp)])
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.backtrack(list, temp, nums, i+1)
            del temp[len(temp)-1]



sol = Solution()
print(sol.subset([1,2,3]))
