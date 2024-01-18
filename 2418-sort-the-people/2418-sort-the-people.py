class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l=0
        for i in range(len(heights)):
            r = l+1
            while r < len(heights):
                if heights[l] < heights[r]:
                    heights[l],heights[r] = heights[r],heights[l]
                    names[l],names[r] = names[r],names[l]
                r+=1
            l+=1
        return names