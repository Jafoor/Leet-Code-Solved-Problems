class Solution {
public:
    int maximalSquare(vector<vector<char>>& v) {
        
        long long n = v.size();
        long long m;
        if(n != 0)
            m = v[0].size();
        else 
            m = 0;
        long long maxlen = 0;
        long long dp[n+1][m+1];
        memset(dp,0,sizeof(dp));
        for(int i= 1;i<=n;i++){
            for(int j = 1; j<=m; j++){
                if(v[i-1][j-1] == '1')
                {
                    dp[i][j] = min(dp[i-1][j],min(dp[i][j-1],dp[i-1][j-1]))+1;
                    maxlen = max(maxlen,dp[i][j]);
                                           
                }
            }
        }
        
        return maxlen*maxlen;
        
    }
};