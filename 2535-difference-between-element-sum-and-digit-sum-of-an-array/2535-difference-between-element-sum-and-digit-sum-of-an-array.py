class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        esum = sum(nums)
        dsum =0
        for i in nums:
            numstr = str(i)
            for char in numstr:
                dsum+=int(char)
        return abs(esum-dsum)