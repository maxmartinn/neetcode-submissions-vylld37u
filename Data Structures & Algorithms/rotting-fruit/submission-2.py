class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        fresh = 0
        time = 0

    
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row, col))
        
        while fresh > 0 and q:
            for i in range(len(q)):
                row, col = q.popleft()
                directions = [
                    [row +1 ,col], [row -1 ,col],[row ,col + 1], [row ,col-1]
                ]
                
                for r, c in directions:
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r, c))
                        fresh -= 1        
            time += 1
        print(fresh)
        return time if fresh == 0 else -1 
        