class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]
        num = pref[0]
        for i in range(1,len(pref)):
            ans.append(num^pref[i])
            num = pref[i]
        return ans