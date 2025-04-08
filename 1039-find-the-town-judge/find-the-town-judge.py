class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outdoor = defaultdict(int)
        indoor = defaultdict(int)
        if n ==1:
            return 1
        for x,y in trust:
            outdoor[x]+=1
            indoor[y]+=1
        for x,y in trust:
            if indoor[y] == n-1 and outdoor[y] == 0:
                return y

        return -1 