class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        first = skill[0] + skill[-1]
        res = skill[0] * skill[-1]
        l,r = 1,len(skill)-2
        while l<r:
            if skill[l] + skill[r] != first:
                return -1
            res += skill[l] * skill[r]
            l+=1
            r-=1
        return res