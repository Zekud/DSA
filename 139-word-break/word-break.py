class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        n = len(s)
        def dp(i,st):
            if st == "":
                return True
            if i > n:
                return False
            if (i,st) in memo:
                return memo[(i,st)]
            take = False
            if st[:i] in wordDict:
                take = dp(1,st[i:])
            not_take = dp(i+1,st)

            memo[(i,st)] = take or not_take
            return memo[(i,st)]
        return dp(0,s)

