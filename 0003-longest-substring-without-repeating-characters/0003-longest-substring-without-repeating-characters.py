class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        chars_index = {}
        l,r = 0,0
        for r in range(len(s)):
            if s[r] in chars_index and chars_index[s[r]] >= l:
                l=chars_index[s[r]]+1
            chars_index[s[r]] = r
            maxlength = max(maxlength,r-l+1)
        return maxlength
            
                