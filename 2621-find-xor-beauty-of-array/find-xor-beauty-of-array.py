class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        x = nums[0]
        for num in nums[1:]:
            x^= num
        return x