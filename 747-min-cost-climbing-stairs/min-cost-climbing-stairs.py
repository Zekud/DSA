class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)
        def dp(i):
            if i == n-1:
                return cost[i]
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = min(cost[i] + dp(i+1), cost[i] + dp(i+2))
            return memo[i]
        return min(dp(0),dp(1))