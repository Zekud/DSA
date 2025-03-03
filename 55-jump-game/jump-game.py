class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums)-1
        reachable = 0
        i = 0
        while i < len(nums) and reachable >= i:
            reachable = max(reachable,i+nums[i])
            print(reachable)
            if reachable >= last:
                return True
            i+=1
        return False