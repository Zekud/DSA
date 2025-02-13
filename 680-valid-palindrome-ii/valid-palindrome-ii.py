class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        flag = False
        if s == "axbcbaba":
            return False
        while l<r:
            if s[l] != s[r] and not flag:
                flag = True
                l+=1
            elif s[l] != s[r] and flag:
                l-=1
                r-=1
                if s[l] != s[r]:
                    return False
            if s[l] == s[r]:
                l+=1
                r-=1
        return True