class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre = {0:1}
        count =tot = 0
        for r in range(len(nums)):
            tot += nums[r]
            if tot - goal in pre:
                count+=pre[tot-goal]
            pre[tot] = pre.get(tot,0) + 1
            
        return count