class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        mx = 1
        for i in range(len(arr)):
            prev = arr[i] - difference
            curr_length = 1
            if prev in dp:
                curr_length += dp[prev]

            dp[arr[i]] = curr_length
            mx = max(mx,curr_length)
        return mx