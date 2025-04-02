class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # Time Complexity: O(nlog(m)) where n is number of mechanics and m is max time
        # Space Complexity: O(1)
        # Helper function as validator
        def enoughTime(m):
            rem = cars
            for time in ranks:
                # For each mechanic its rank*(car^2) shouldn't exceed the time - m
                calc = int(pow(m//time, 0.5))
                rem -= calc
            return rem <= 0
        
        # Our output space starts form 1 (#Ref: constriants) and ends with max(ranks)*(cars^2) is max it can get (multiplying the higher rank with the square of the entire car number).
        l, h = 1, max(ranks)*pow(cars,2)
        while l<=h:
            m = (l+h)//2
            if enoughTime(m): h = m-1
            else: l = m+1
        return l