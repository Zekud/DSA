class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxaverage =  float('-inf')
        total = 0
        l,r= 0,0
        for r in range(len(nums)):
            total+=nums[r]
            if r-l+1 == k:
                maxaverage = max(maxaverage, (total/k))
                total-=nums[l]
                l+=1
            
        return maxaverage