class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        count = 0
        if len(nums) == 1:
            return 1
        l = 0
        x = nums[0]
        for r in range(1,len(nums)):         
            while (nums[r] & x) !=0:
                x^=nums[l]
                l+=1
            x|=nums[r]
            count = max(r-l+1,count)

        return count
