class Solution:
    def maximum69Number (self, num: int) -> int:
        maximum = num
        n = len(str(num))
        i = 0
        while i<n:
            numstr = list(str(num))
            
            if numstr[i] == '9':
                numstr[i] = '6'
                numstr = ''.join(numstr)
                maximum = max(maximum,int(numstr))
            else:
                numstr[i] = '9'
                numstr = ''.join(numstr)
                maximum = max(maximum,int(numstr))
            i+=1
        return maximum