class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        r=int(str(num)[::-1])
        rr=int(str(r)[::-1])

        if num==rr:
            return True

        else:
            return False
        
        