class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []
        for i in range(len(grid)):
            rev = grid[i]
            rev.sort(reverse=True)
            print(rev)
            for j in range(limits[i]):
                heappush(heap,rev[j])
                if len(heap) > k:
                    heappop(heap)
        return sum(heap)
               