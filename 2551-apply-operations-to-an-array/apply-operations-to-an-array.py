class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i],nums[i+1] = 2*nums[i], 0
        return sorted(nums,key=lambda x: x==0)
