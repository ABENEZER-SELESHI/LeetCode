class SeatManager:

    def __init__(self, n: int):
        self.heqp = [i for i in range(1, n+1)]
        heapify(self.heqp)

    def reserve(self) -> int:
        return heappop(self.heqp)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.heqp, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)