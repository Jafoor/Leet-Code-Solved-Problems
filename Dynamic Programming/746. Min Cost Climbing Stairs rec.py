class Solution(object):
    def minCostClimbingStairs(self, cost):
        memo = [0]*(len(cost)+10)
        m1 = solve(0,cost,memo)
        m2 = solve(1,cost,memo)
        return min(m1,m2)
def solve(i,cost,memo):
    if i>=len(cost):
        return 0
    if memo[i] == 0:
        x1 = cost[i] + solve(i+1,cost,memo)
        x2 = cost[i] + solve(i+2,cost,memo)
        memo[i] = min(x1,x2)
    return memo[i]
 