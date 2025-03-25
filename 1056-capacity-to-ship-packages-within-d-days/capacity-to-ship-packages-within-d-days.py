class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validate(mid):
            nonlocal days
            curr_sum = 0
            count = 1
            for weight in weights:
                if curr_sum + weight <= mid:
                    curr_sum += weight
                else:
                    curr_sum = weight
                    count+=1
            return count <= days
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high)//2
            if validate(mid):
                high = mid -1
            else:
                low = mid+1
        return low

