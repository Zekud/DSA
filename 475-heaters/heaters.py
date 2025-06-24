class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        max_radius =0
        for house in houses:
            index = bisect_left(heaters, house)

            if index ==0:
                rad = heaters[0] - house
            elif index ==len(heaters):
                rad = house - heaters[-1]
            else:
                rad = min(heaters[index] - house,house - heaters[index-1])
            max_radius = max(max_radius, rad)
        return max_radius


        