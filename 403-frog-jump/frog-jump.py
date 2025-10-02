class Solution:
    def canCross(self, stones: List[int]) -> bool:
       
        memo = {}
        st = defaultdict(int)
        for i,v in enumerate(stones):
            st[v] = i
        n = len(stones)
        if 1 not in st:
            return False
        def dp(i,j):
            if i == n-1:
                return True
            if i >= n:
                return False
            if j <= 0:
                return False
            if (i,j) in memo:
                return memo[(i,j)]
            res = False
            if (stones[i] + j-1) in st:
                res = dp(st[stones[i]+j-1],j-1)
            if (stones[i] + j) in st:
                res |= dp(st[stones[i] + j],j)
            if (stones[i] + j+1) in st:
                res |= dp(st[stones[i] + j+1],j+1)
            memo[(i,j)] = res
            return res

        return dp(1,1)
