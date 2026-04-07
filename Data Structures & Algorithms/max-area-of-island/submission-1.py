class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # iterate through all potential island starting points

        # check if current pair is already visited

        # return the sum of the 4 directions
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(r, c):
            if r < 0 or r == ROWS or c == COLS or c < 0 or grid[r][c] != 1:
                return 0
            grid[r][c] = -1
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    res = max(area, res)
        return res