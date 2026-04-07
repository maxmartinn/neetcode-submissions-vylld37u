class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        res = 0

        def bfs(row, col):
            if (row, col) in visited:
                return
            if row not in range(ROWS):
                return
            if col not in range(COLS):
                return
            if grid[row][col] == "0":
                return
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            visited.add((row, col))
            for d in directions:
                bfs(row + d[0], col + d[1])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    res += 1
                    bfs(row, col)
                   
        return res