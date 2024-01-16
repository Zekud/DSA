class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        chars_index = dict()
        result = []
        chars_index[nums[0]] = 0
        for i in range(1,len(nums)):
            if target-nums[i] in chars_index:
                num1 = target-nums[i]
                result.append(chars_index[num1])
                result.append(i)
                break
            else:
                chars_index[nums[i]] = i
        return result