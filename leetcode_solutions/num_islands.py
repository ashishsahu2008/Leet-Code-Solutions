class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.len_row = len(grid)
        if self.len_row == 0:
            return 0
        self.len_col = len(grid[0])
        # self.boolean_matrix = [[False for x in range(self.len_col)] for y in range(self.len_row)]
        self.output = 0
        for x in range(self.len_row):
            for y in range(self.len_col):
                if grid[x][y] == '1':
                    self.backtrack(grid, x, y)
                    self.output +=1
        return self.output

    def backtrack(self, grid, start_row, start_column):
        if start_row < 0 or start_column < 0 or start_row >= self.len_row or start_column >= self.len_col or                                  grid[start_row][start_column] == '0':
            return
        grid[start_row][start_column] = '0'
        self.backtrack(grid, start_row + 1, start_column)
        self.backtrack(grid, start_row - 1, start_column)
        self.backtrack(grid, start_row, start_column + 1)
        self.backtrack(grid, start_row, start_column - 1)
        
