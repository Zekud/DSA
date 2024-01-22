class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        totalsums = {0:1}
        count = 0
        cumulative = 0
        for n in nums:
            cumulative+=n
            if (cumulative - k) in totalsums:
                count+= totalsums[cumulative-k]
            totalsums[cumulative] = totalsums.get(cumulative,0)+1
        return count
            