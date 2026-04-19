import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        # Min-heap: (max_elevation_so_far, row, col)
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while heap:
            time, r, c = heapq.heappop(heap)
            
            # Reached destination
            if r == n - 1 and c == n - 1:
                return time
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    # Time to reach neighbor = max of current time and neighbor's elevation
                    heapq.heappush(heap, (max(time, grid[nr][nc]), nr, nc))
        
        return -1  # Unreachable (won't happen given constraints)