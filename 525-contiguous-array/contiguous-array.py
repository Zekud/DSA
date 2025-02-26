class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_index = {0:-1}
        tot = 0
        maxl = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                tot -= 1
            else:
                tot +=1

            if tot in sum_index:
                maxl = max(maxl, i - sum_index[tot])
            else:
                sum_index[tot] = i
        return maxl