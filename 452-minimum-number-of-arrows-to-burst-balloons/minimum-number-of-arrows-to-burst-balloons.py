class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0],x[1]))
        if len(points) == 1:
            return 1
        l,r = 0,1
        arrows = 1 
        while r < len(points):
            if points[r][0] > points[l][1]:
                arrows+=1
                l=r
            else:
                if points[r][1] < points[l][1]:
                    l=r
            
            r+=1
        return arrows 
