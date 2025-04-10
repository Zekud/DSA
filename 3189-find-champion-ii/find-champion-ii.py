class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indoor = set()
        outdoor = set()
        winner = []
        for x,y in edges:
            outdoor.add(x)
            indoor.add(y)
        for i in range(n):
            if i not in indoor or i not in outdoor:
                outdoor.add(i)
        for i in outdoor:
            if i not in indoor:
                winner.append(i)
        if len(winner) == 1:
            return winner[0]
        else:
            return -1