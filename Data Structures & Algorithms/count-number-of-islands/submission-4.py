class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        visited = set()
        
        def bfs(row, col):
            if row not in range(ROWS) or col not in range(COLS):
                return
            if (row, col) in visited or grid[row][col] == "0":
                return
            directions = [
                [1, 0], [-1, 0], [0, -1], [0, 1]
            ]
            visited.add((row, col))
            for dr, dc in directions:
                bfs(row + dr, col + dc)
            

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    res += 1
        return res