class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # memo = {}
        # def backtrack(curr):
        #     if curr == 0:
        #         return 1
        #     if curr < 0:
        #         return 0
        #     if curr in memo:
        #         return memo[curr]
        #     memo[curr] = 0
            
        #     for i in range(len(nums)):
        #         memo[curr] += backtrack(curr-nums[i])
            
        #     return memo[curr]
        # return backtrack(target)
        # bottom up
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1,len(dp)):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i-num]
        return dp[target]


