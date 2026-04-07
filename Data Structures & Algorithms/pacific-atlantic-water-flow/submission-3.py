class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()

        ROWS = len(heights)
        COLS = len(heights[0])
        # check if water can be flown from the starting indexes of each possible position for both atl and pac
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

        return [list(x) for x in pac & atl]