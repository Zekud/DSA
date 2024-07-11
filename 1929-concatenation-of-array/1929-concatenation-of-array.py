class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        j = len(nums)
        for i in range(j):
            nums.append(nums[i])
        return nums