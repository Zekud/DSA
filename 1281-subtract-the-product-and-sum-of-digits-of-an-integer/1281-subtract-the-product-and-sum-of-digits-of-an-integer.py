class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        numstr = str(n)
        product,total = 1,0
        for char in numstr:
            product*= int(char)
        for char in numstr:
            total+=int(char)
        return product - total