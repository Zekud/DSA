class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        sweep = [0]* (len(s) + 2)
        for l,r,d in shifts:
            if d == 0:
                sweep[l] -=1
                sweep [r+1] +=1
            else:
                sweep[l] +=1
                sweep[r+1] -= 1

        for i in range(1,len(sweep)):
            sweep[i] += sweep [i-1]
        arr = []
        for i in range(len(s)):
            c = ((ord(s[i])-97) + sweep[i]) %26
            arr.append(chr(c + 97))
        return "".join(arr)