class UndergroundSystem:
​
    def __init__(self):
        #trips map of (start_loc, end_loc) : (total length, num of trip)
        self.trips = collections.defaultdict(lambda : (0,0))
        # id : (stationName: time)
        self.curPeople = {}
        
​
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.curPeople[id] = (stationName, t)
        return
        
        
        
​
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_loc, start_time = self.curPeople[id]
        total_time, freq = self.trips[(start_loc, stationName)]
        total_time += (t-start_time)
        freq += 1
        self.trips[(start_loc, stationName)] = (total_time, freq)
        return
        
        
​
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, freq = self.trips[(startStation, endStation)]
        return total_time / freq
​
​
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
