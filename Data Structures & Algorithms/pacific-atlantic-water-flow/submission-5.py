class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Clarification

        return a list of every cell that can flow water from the pacific ocean to the atlantic ocean

        start from cell and see if there is a route that can lead that cell to the pacific and atlatnic ocean

        cells can reach an ocean if theres a path of decreasing heights

        plan

        iterate from the cells that border an ocean

        see if there is a larger cell in its path

        add to respective ocean set

        return the intersection of both atl and pac sets
        """

        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visited):
            nei = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            visited.add((r, c))
            for nr, nc in nei:
                if nr == -1 or nr == ROWS or nc == -1 or nc == COLS:
                    continue
                if (nr, nc) in visited or heights[nr][nc] < heights[r][c]:
                    continue
                dfs(nr, nc, visited)

        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS - 1, atl)
        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS - 1, c, atl)
        return list(pac & atl)
"""

        Input: heights = [
  [0,2],
  [3,4],
]

[[0, 1], [1, 0],[1,1]]

"""
