class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        currsum = 0
        for n in nums:
            currsum = max(currsum,0) + n
            maxsum = max(maxsum,currsum)
        return maxsum
            