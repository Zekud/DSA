class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        lastIndex = len(nums) -1
        i=0
        while i < len(nums) and i <= reachable:
            reachable = max(reachable, nums[i]+i)
            if reachable >= lastIndex:
                return True
            i+=1
        return False
    
        # O(n) Time complexity
        # O(1) space complexity