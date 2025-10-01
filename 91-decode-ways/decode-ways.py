class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        memo = {}
        n = len(s)
        def dp(i):
            if i < n and s[i] == "0":
                return 0
            if i >= n-1:
                return 1
            if i in memo:
                return memo[i]
            onetake = dp(i+1)
            twotake = 0

            if int(s[i:i+2]) <= 26:
                twotake = dp(i+2)
            memo[i] = onetake + twotake
            return memo[i]
        return dp(0)