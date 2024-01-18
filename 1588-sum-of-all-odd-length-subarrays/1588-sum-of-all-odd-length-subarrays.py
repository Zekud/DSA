class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        i = 1
        while i <= len(arr):
            start = 0
            while start <= len(arr)-i:
                sub = arr[start:start+i]
                total+=sum(sub)
                start+=1
            i+=2
        return total