class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        leftP= 1
        for i in range(len(nums)):
            result.append(leftP)
            leftP*=nums[i]
        i=len(nums)-1
        rightP = 1
        while i>=0:
            result[i] = result[i] * rightP
            rightP*=nums[i]
            i-=1
        return result