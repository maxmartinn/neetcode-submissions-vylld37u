class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visit = set()

        def addRoom(row, col):
            if (row not in range(ROWS) or 
                col not in range(COLS) or
                (row, col) in visit or
                grid[row][col] == -1):
                return
            visit.add((row,col))
            q.append([row, col])
                

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append([row,col])
                    visit.add((row,col))
 
        count = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = count
                addRoom(row + 1, col)
                addRoom(row - 1, col)
                addRoom(row, col + 1)
                addRoom(row, col - 1)
            count += 1

