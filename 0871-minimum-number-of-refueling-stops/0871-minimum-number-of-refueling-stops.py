class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        '''
        stations is [location, fuel]
        append target to stations to see if you can drive by it

        Intution can drive by stations until you run of gas

        Algo:
        Store stations with most fuel in max heap
        Calculate how much gas you have left at a certain spot
            -if out of gas (fuel < 0) can retroactively fill fuel by looking at past large gas stastions
            -if heap is empty and fule is still < 0 there is no solution

        Time: O(NlogN) to iterate through stastions & heap operations
        Space: O(N) in worst case use heap
        '''
        stations.append([target, float('inf')])
        prev, curFuel = 0, startFuel
        maxHeap = []
        stops = 0

        for location, fuel in stations:
            distance = location - prev
            curFuel -= distance
            while maxHeap and curFuel < 0:
                curFuel += -heapq.heappop(maxHeap)
                stops += 1
            # No solution :\ ran out of gas stations
            if curFuel < 0:
                return -1
            # Add this station to our pq to come back to later if needed
            prev = location
            heapq.heappush(maxHeap, -fuel)

        return stops

        