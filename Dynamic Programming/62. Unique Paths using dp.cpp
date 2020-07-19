class Solution {
public:
    int uniquePaths(int m, int n) {
        long long dp[n+1][m+1] ;
        memset(dp,0,sizeof(dp));
        for(int i = 0; i<m-1;i++)
        {
            dp[n-1][i] = 1;
        }
        for(int i=0;i<n;i++)
        {
            dp[i][m-1] = 1;
        }
        
        for(int i=n-2;i>=0;i--)
        {
            for(int j=m-2;j>=0;j--)
            {
                dp[i][j] = dp[i+1][j]+dp[i][j+1];
            }
        }
        
        return dp[0][0];
    }
};