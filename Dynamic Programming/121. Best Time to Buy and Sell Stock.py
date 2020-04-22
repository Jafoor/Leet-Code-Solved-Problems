class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        if not prices:
            return 0
        mx = prices[0]
        mn = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < mn :
                mn = mx = prices[i]
            else:
                mx = max(prices[i], mx)
            x = mx - mn
            ans = max(ans,x)
        return ans
                
            
        