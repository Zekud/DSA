class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heappush(self.left,-num)
        if self.right and -self.left[0] > self.right[0]:
            heappush(self.right,-heappop(self.left))
        
        if len(self.left) > len(self.right)+1:
            n = -heappop(self.left)
            heappush(self.right, n)
        elif len(self.right) > len(self.left):
            heappush(self.left, -heappop(self.right))

    def findMedian(self) -> float:
        if (len(self.right) + len(self.left)) % 2 != 0:
            return -self.left[0]/1
        else:
            return (-self.left[0] + self.right[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()