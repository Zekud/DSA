class Solution:
    def countDigits(self, num: int) -> int:
        numstr = str(num)
        count = 0
        for char in numstr:
            if num%int(char)==0:
                count+=1
        return count