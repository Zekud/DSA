class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = [0]*(max(nums) + 1)
        res = []
        for i in nums:
            count[i] +=1
        for index, value in enumerate(count):
            if value == 2:
                res.append(index)
        return res