class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = [0] * (max(citations)+1)
        for num in citations:
            count[num] +=1
        target = 0
        for i,v in enumerate(count):
            for j in range(v):
                citations[target] = i
                target+=1
        n = len(citations)
        for i in range(n):
            if n- i <= citations[i]:
                return n - i
        return 0

