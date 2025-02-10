class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        s_sorted = sorted(count.items(), key = lambda x: x[1], reverse=True)
        s=""
        for key, val in s_sorted:
            s += key * val
        return s