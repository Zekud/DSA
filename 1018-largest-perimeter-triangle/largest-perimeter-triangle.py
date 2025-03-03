class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        j = len(nums)-3
        mx = 0
        while j >= 0:
            if nums[j] + nums[j+1] > nums[j+2]:
                mx = nums[j] + nums[j+1] + nums[j+2]
                break
            j-=1
        return mx
