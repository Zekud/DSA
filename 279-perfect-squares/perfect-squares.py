class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        for i in range(1,n+1):
            j = 1
            while j**2 <= i:
                dp[i] = min(dp[i],1+ dp[i-j**2])
                j+=1
        return dp[n]