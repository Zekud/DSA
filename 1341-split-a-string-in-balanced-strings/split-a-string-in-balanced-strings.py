class Solution:
    def balancedStringSplit(self, s: str) -> int:
        mx = 0
        count = Counter(s)
        for char in s:
            count[char]-=1
            if count["L"] == count["R"]:
                mx+=1
        return mx
        