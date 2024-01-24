class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total = 0
        for n in nums:
            total+=n
            result.append(total)
        return result