class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = [0]*(max(costs)+1)
        for num in costs:
            count[num]+=1
        target=0
        for i,v in enumerate(count):
            for j in range(v):
                costs[target] = i
                target+=1
        count = 0
        for i in costs:
            if i <= coins:
                count+=1
                coins-=i
        return count
            
