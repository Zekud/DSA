class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
      
        prefixsum = []
        total = 0
        for n in nums:
            total+=n
            prefixsum.append(total)
        leftsum = 0
        for i in range(len(nums)):
            rightsum = total - leftsum - nums[i]
            if rightsum == leftsum:
                return i
            leftsum+=nums[i]
        return -1
            