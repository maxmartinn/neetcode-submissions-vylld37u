class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visited = set()
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
                    if nr == -1 or nc == -1 or nr == ROWS or nc == COLS or (nr, nc) in visited or grid[nr][nc] == -1:
                        continue    
                    q.append((nr, nc))
                    visited.add((nr, nc))
            dist += 1

