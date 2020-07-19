//Recursive Process

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& v) {
        
        int n = v.size();
        int m = v[0].size();
        if (n == 0 or m == 0){
            return 0;
        }
        long long dp [101][101];
        memset(dp,-1,sizeof(dp));
        return solve(v,0,0,n-1,m-1,dp);
    }
    
    int solve(vector<vector<int>>& v,int i,int j,int n,int m,long long dp[101][101]){
        if(dp[i][j] != -1){
            return dp[i][j];
        }
        if (i == n and j == m){
            if (v[i][j] == 0)
                return 1;
            else
                return 0;
        }
        
        if (i>n or j>m)
            return 0;
        
        if (v[i][j] == 1){
            dp[i][j] = 0;
            return 0;
        }
        
        long long left = solve(v,i+1,j,n,m,dp);
        long long right = solve(v,i,j+1,n,m,dp);
        dp[i][j] = left + right;
        return left + right;
    }
    
};