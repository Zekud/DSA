class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l,r =0,0
        profit = 0
        while r<len(prices):
            if prices[r]<prices[l]:
                l=r
            profit = max(profit,prices[r]-prices[l])
            r+=1
        return profit
        
        