class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = Counter(s)
        arr = []
        for i in range(count["1"]-1):
            arr.append("1")
        for i in range(count["0"]):
            arr.append("0")
        arr.append("1")
        return "".join(arr)