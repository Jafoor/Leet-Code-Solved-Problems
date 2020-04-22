class Solution:
    def divisorGame(self, N: int) -> bool:
        #solution using dp
        dp = [0,0,1,0]
        for i in range(4,N+1):
            if dp[i-1] == 0:
                dp.append(1)
            else:
                dp.append(0)
        return dp[N] == 1
            
            