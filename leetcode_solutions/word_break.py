class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        b = [False for i in range(len(s)+1)]
        b[0] = True
        for i in range(len(s)+1):
            for j in range(i):
                if b[j] and (s[j:i] in wordDict):
                    b[i] = True
                    break
        return b[len(s)]
