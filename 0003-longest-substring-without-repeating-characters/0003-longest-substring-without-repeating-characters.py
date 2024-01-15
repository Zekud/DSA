class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        chars = dict()
        l,r = 0,0
        while r < len(s):
            if s[r] in chars:
                count = max(count, r-l)
                l+=1
                r=l
                chars.clear()
            else:
                chars[s[r]] = 1
                r+=1
        return max(len(chars),count)
            
                