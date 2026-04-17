class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647
        q = deque()
        visited = set() # (r, c)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for nr, nc in neighbors:
                    if 0 <= nr <= ROWS - 1 and 0 <= nc <= COLS -1 and (nr, nc) not in visited and grid[nr][nc] != -1:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            dist += 1