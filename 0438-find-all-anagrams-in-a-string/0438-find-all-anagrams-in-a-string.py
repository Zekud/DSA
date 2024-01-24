class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = []
        target = Counter(p)
        window = Counter()
        l,r = 0,0
        for r in range(len(s)):
            window[s[r]]+=1
            if r -l+1 == len(p):
                if window == target:
                    indices.append(l)
                window[s[l]]-=1
                if window[s[l]] == 0:
                    del window[s[l]]
                l+=1
        return indices