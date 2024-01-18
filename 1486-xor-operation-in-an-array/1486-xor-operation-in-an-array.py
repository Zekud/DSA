class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = []
        for i in range(n):
            arr.append(start + 2*i)
        result = 0
        for i in arr:
            result^= i
        return result