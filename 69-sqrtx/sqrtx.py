class Solution:
    def mySqrt(self, x: int) -> int:
        if x <=1 :
            return x
        start,end = 1,x//2+1
        ans = -1
        while start<=end:
            mid = (start + end)//2
            if mid * mid == x:
                return mid
            elif mid*mid > x:
                end = mid-1
            else:
                ans = mid
                start = mid+1
        return ans