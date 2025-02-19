class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.prefix = []
        self.tot = 1
    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = []
            self.tot = 1
        else:
            self.tot *= num
            self.prefix.append(self.tot)

        self.arr.append(num)

    def getProduct(self, k: int) -> int:
        if k > len(self.prefix):
            return 0
        if (len(self.prefix) - k ) == 0:
            return self.prefix[-1]
        return self.prefix[-1] // self.prefix[len(self.prefix)-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)