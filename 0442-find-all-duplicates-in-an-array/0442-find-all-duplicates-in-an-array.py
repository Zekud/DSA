class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if nums[index] < 0:
                lst.append(abs(nums[i]))
            else:
                nums[index] = -1 * nums[index]
        return lst