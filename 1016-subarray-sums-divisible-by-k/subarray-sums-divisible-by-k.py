class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder = defaultdict(int)
        remainder[0] +=1
        tot = 0
        count = 0
        for num in nums:
            tot += num
            if tot % k in remainder:
                count += remainder[tot%k]
            remainder[tot%k] +=1
        return count
