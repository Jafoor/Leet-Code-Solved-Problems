class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n,m = len(grid), len(grid[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0:
                    if j == 0:
                        dp[i][j] = grid[i][j]
                    else:
                        dp[i][j] = dp[i][j-1]+grid[i][j]
                else:
                    if j == 0:
                        dp[i][j] = dp[i-1][j] + grid[i][j]
                    else:
                        dp[i][j] = min(dp[i-1][j] , dp[i][j-1]) + grid[i][j]
        return dp[n-1][m-1]