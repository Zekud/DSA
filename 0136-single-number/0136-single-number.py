class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lastNum = 0
        for i in range(len(nums)):
            lastNum ^= nums[i]
        return lastNum