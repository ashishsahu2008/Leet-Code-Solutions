class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        dist = 1
        reached = []
        reached.append(beginWord)
        wordList.append(endWord)
        while endWord not in reached:
            addTo = []
            for each in reached:
                print(reached)
                for i in range(len(each)):
                    ch = each
                    for code in range(ord('a'), ord('z') + 1):
                        ch = list(ch)
                        ch[i] = chr(code)
                        ch = ''.join(ch)
                        if ch in wordList:
                            addTo.append(ch)
                            wordList.remove(ch)
            dist +=1
            if len(addTo) == 0:
                return 0
            reached = addTo
        return dist




beginWord = 'hit'
endWord = 'cog'
wordList = ["hot","dot","dog","lot","log"]
sol = Solution()
print(sol.ladderLength(beginWord, endWord, wordList))
