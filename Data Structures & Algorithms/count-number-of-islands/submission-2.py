class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        visited = set()
        def bfs(row, col):
            if row not in range(ROWS) or col not in range(COLS):
                return
            if grid[row][col] == "0" or (row, col) in visited:
                return
            visited.add((row, col))

            directions = [
                [-1,0], [1,0], [0, 1], [0, -1]
            ]

            for dr, dc in directions:
                bfs(row+dr, col+dc)

        if not grid or not len(grid[0]):
            return islands
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1
                    bfs(row, col)
        return islands