class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        
        def canReach(t):
            if grid[0][0] > t: return False
            visited = {(0, 0)}
            stack = [(0, 0)]
            while stack:
                r, c = stack.pop()
                if (r, c) == (n-1, n-1): return True
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited and grid[nr][nc] <= t:
                        visited.add((nr, nc))
                        stack.append((nr, nc))
            return False
        
        lo, hi = 0, n*n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if canReach(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
            