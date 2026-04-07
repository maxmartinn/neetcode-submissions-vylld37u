class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        res = 0
        def bfs(row, col):
            if row not in range(ROWS) or col not in range(COLS) or (row, col) in visited or grid[row][col] == "0":
                return
            visited.add((row, col))
            bfs(row - 1, col)
            bfs(row+1, col)
            bfs(row, col-1)
            bfs(row , col+1)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    res += 1
                    bfs(i, j)
                
        return res