class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        i,j =1,len(piles)-1
        tot = 0
        while i<j:
            tot+=piles[i]
            i+=2
            j-=1
        return tot
        