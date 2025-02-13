class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        mx = 0
        l,r = 0,0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l+=1
            chars.add(s[r])
            mx = max(mx,len(chars))
        return mx
