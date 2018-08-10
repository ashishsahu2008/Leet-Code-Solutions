'''
https://leetcode.com/problems/group-anagrams/description/
'''
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47, 53, 59, 61, 67, 71, 73, 79,83, 89, 97, 103]
        for s in strs:
            k =1
            for c in s:
                k *= prime[ord(c) - ord('a')]
            if k in dic:
                l = dic.get(k)
                l.append(s)
            else:
                dic[k] = [s]
        return list(dic.values())

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
