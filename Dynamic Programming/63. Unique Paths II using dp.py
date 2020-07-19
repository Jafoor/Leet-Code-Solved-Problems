class Solution:
    def uniquePathsWithObstacles(self, dp: List[List[int]]) -> int:
        n = len(dp)
        m = len(dp[0])
        
        if dp[0][0]==1:
            return 0
        dp[0][0] = 1
        for i in range(1,m):
            if dp[0][i-1] == 1 and dp[0][i] == 0:
                dp[0][i] = 1
            else:
                dp[0][i] = 0
        for i in range(1,n):
            if dp[i-1][0] == 1 and dp[i][0]==0:
                dp[i][0] = 1
            else:
                dp[i][0] = 0
        for i in range(1,n):
            for j in range(1,m):
                if dp[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        
        return dp[n-1][m-1];
            
        