class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numbers = {}
        for num in nums:
            if num in numbers:
                return True
            numbers[num] = 1
        return False