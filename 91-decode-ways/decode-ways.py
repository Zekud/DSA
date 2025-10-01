class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        # memo = {}
        # n = len(s)
        # def dp(i):
        #     if i < n and s[i] == "0":
        #         return 0
        #     if i >= n-1:
        #         return 1
        #     if i in memo:
        #         return memo[i]
        #     onetake = dp(i+1)
        #     twotake = 0

        #     if int(s[i:i+2]) <= 26:
        #         twotake = dp(i+2)
        #     memo[i] = onetake + twotake
        #     return memo[i]
        # return dp(0)
        n = len(s)
        dp = [0] * (n+1)
        dp[-1] = 1
        for i in range(n-1,-1,-1):
            if s[i] == "0":
                continue
            dp[i] = dp[i+1]
            if int(s[i:i+2]) <= 26 and i+2 <= n:
                dp[i] += dp[i+2]
        print(dp)
        return dp[0]
