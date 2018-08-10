class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        b = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.backtrack(board, word, 0, i, j, b):
                    return True
        return False

    def backtrack(self, board, word, word_ptr, start, end, b):
        if word_ptr == len(word):
            return True
        if start < 0 or start >= len(board) or end < 0 or end >= len(board[0]) or b[start][end] or word[word_ptr] != board[start][end]:
            return False
        b[start][end] = True
        # word_ptr += 1
        if self.backtrack(board, word, word_ptr+1, start+1, end, b) \
        or self.backtrack(board, word, word_ptr, start-1, end, b) \
        or self.backtrack(board, word, word_ptr, start, end+1, b) \
        or self.backtrack(board, word, word_ptr, start, end-1, b):
                return True
        b[start][end] = False

sol = Solution()
print(sol.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEF"))
