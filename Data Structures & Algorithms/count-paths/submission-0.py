class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * m for _ in range(n)]
        dp[-1][-1] = 1
        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                directions = [[1,0], [-1,0], [0, -1], [0, 1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < n and 0 <= col < m:
                        dp[r][c] += dp[row][col]
        return dp[0][0]