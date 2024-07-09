class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        c = Counter(nums)
        m = [i for i in c if c[i] == max(c.values())]
        return min([len(nums)-nums[::-1].index(x) - nums.index(x) for x in m])