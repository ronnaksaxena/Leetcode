class SeatManager:

    def __init__(self, n: int):
        self.n = n
        self.reservedSeats = set()
        self.nextLowest = [i for i in range(1,self.n+1)]
        heapq.heapify(self.nextLowest)
        

    def reserve(self) -> int:
        # update lowest seat to next lowest
        reservedSeat = heapq.heappop(self.nextLowest)
        while reservedSeat in self.reservedSeats:
            reservedSeat = heapq.heappop(self.nextLowest)
        self.reservedSeats.add(reservedSeat)
        return reservedSeat
        

    def unreserve(self, seatNumber: int) -> None:
        self.reservedSeats.remove(seatNumber)
        heapq.heappush(self.nextLowest, seatNumber)
        return
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)