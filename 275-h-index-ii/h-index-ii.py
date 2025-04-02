class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def check(i):
            if len(citations) - i > citations[i]:
                return True
            else:
                False
        low, high = 0,len(citations)-1
        while low<=high:
            mid = (low+high)//2
            if check(mid):
                low = mid+1
            else:
                high = mid-1
        return len(citations) - low
