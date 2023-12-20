class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l1 = list(filter(lambda x : x>0, nums))
        l2 = list(filter(lambda x: x<0, nums))
        return max(len(l1),len(l2))