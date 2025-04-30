class SeatManager:

    def __init__(self, n: int):
        self.available = [i for i in range(1,n+1)]
        self.reserved = {}

    def reserve(self) -> int:
        seat = heappop(self.available)
        # print(self.available)
        self.reserved[seat] = seat
        return seat

    def unreserve(self, seatNumber: int) -> None:
        seat = self.reserved[seatNumber]
        del self.reserved[seatNumber]
        # print(self.reserved)
        heappush(self.available,seat)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)