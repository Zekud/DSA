class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i = 1
        while True:
            num = n*i
            if num%2==0:
                return num
            i+=1
            