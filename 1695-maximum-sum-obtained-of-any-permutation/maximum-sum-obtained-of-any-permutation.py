class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        sweep = [0] *(len(nums)+2)
        for l,r in requests:
            sweep[l] +=1
            sweep[r+1] -=1
        for i in range(1,len(sweep)):
            sweep[i] += sweep[i-1]
        tot = 0
        nums.sort(reverse = True)
        sweep.sort(reverse = True)
        for i in range(len(nums)):
            tot += nums[i] * sweep[i]
        return tot % (10**9 + 7)