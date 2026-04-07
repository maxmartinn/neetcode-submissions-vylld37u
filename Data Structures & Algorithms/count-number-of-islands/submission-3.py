class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        visited = set()
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            while q:
                row, col = q.popleft()
                directions = [
                    [-1,0], [1,0], [0, 1], [0, -1]
                ]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r not in range(ROWS) or c not in range(COLS):
                        continue
                    if grid[r][c] == "0" or (r, c) in visited:
                        continue
                    q.append((r, c))
                    visited.add((r, c))

        if not grid or not len(grid[0]):
            return islands
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        return islands