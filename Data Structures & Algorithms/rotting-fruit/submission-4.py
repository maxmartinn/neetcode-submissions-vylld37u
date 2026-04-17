class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visited = set()
        oranges = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    oranges += 1
        t = 0
        while q and oranges:
            for _ in range(len(q)):
                r, c = q.popleft()
                neighbors = [(r + 1,c), (r - 1,c), (r,c + 1), (r,c - 1)]
                for nr, nc in neighbors:
                    if nr == -1 or nc == -1 or nr == ROWS or nc == COLS or (nr, nc) in visited or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    visited.add((nr, nc))
                    q.append((nr, nc))
                    oranges -= 1
            t += 1
        return -1 if oranges else t