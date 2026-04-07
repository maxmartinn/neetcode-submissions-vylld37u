class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # iterate through all starting positions and then mark cells if its apart of the island.

        # if the cell has been marked do not do another traversal

        # add to visit area if traversed
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set() # {(r, c)}
        res = 0
        def dfs(r, c):
            if r == ROWS or r == -1 or c == COLS or c == -1:
                return
            if (r, c) in visit or grid[r][c] == "0":
                return
            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visit or grid[r][c] == "0":
                    continue
                res += 1
                dfs(r, c)
        return res

        """
        Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4
        """

