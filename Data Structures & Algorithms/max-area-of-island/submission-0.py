class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        visited = set()

        def bfs(row, col):
            if row not in range(ROWS) or col not in range(COLS):
                return 0
            if (row, col) in visited or grid[row][col] == 0:
                return 0
            directions = [
                [0, 1], [1,0 ], [0, -1], [-1,0 ]
            ]
            res = 1
            visited.add((row, col))
            for dr, dc in directions:
                res += bfs(row+dr, col+dc)
            return res

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    res = max(res, bfs(row, col))
        return res