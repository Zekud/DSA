class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapify(nums)
        while len(nums) > 1:
            first_min = heappop(nums)
            if first_min >= k:
                break
            second_min = heappop(nums)
            heappush(nums,((first_min*2)+second_min))
            count+=1
        return count
            