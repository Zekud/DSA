class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # top down
        # memo = {}
        # n = len(questions)
        # def dp(i):
        #     if i >= n:
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     # not take
        #     res = dp(i+1)

        #     # take
        #     memo[i] = max(res,questions[i][0] + dp(i+questions[i][1]+1))
        #     return memo[i]
        # return dp(0)
        # bottom up
        n = len(questions)
        dp = [0] * (n+1) #so we can handle the base case dp[n]=0
        for i in range(n-1,-1,-1):
            pts = questions[i][0]
            bp = questions[i][1]
            # not take
            nottake = dp[i+1]
            # take
            take = pts
            if i + bp + 1 <=n:
                take = pts + dp[i + bp + 1]
            dp[i] = max(take,nottake)
        return dp[0]


