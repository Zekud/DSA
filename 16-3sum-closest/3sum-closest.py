class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            val = nums[i]

            while l < r:
                x = nums[l] + nums[r] + val
                if x < target:
                    l += 1
                else:
                    r -= 1
                if abs(target - x) < abs(target - closest):
                    closest = x
        return closest