class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        st = [0] * (n+1)
        st[1],st[2] = 1,2
        for i in range(3,n+1):
            st[i] = st[i-1] + st[i-2]
        return st[n]
        
        