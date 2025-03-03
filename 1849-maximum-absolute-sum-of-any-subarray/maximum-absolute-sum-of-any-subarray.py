class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxsum = 0
        minsum = 0
        currsum = 0
        for n in nums:
            currsum += n
            maxsum = max(maxsum,currsum)
            minsum = min(minsum,currsum)
        return maxsum - minsum
