class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        stops = 0
        maxHeap = []
        stations.append([target, 0])
        tank = startFuel
        prevLocation = 0

        for location, fuel in stations:
            tank -= (location-prevLocation)
            while tank < 0 and maxHeap:
                tank += -heapq.heappop(maxHeap)
                stops += 1
            if tank < 0:
                return -1
            if location == target:
                return stops
            prevLocation = location
            heapq.heappush(maxHeap, -fuel)

        return stops



        