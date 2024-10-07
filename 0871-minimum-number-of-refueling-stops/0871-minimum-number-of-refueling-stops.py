class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        '''
        Clarification Qs:
        - input: target int, startFueld int, stattions [[int, int]]
        - output: int (stops)
        - car starts at position 0. {-1, 100000} => always moves forward positive
        - garunteed one station per location
        - station is any order
        - target is always positive number

        target = 100, startFuel = 10, 
        stations = [[10,60],[20,30],[30,30],[60,40]]

        Brute Force
        station append target
        minNumber of stops (locationI, curTank)
            if curTank < 0:
                return inf
            if locationI == len(stations) - 1:
                return 0
            either stop or not stop
            return min(fn(location+1, curTank - (location[i+1] - location[i]),
            1 + fn(location+1, curTank + staions[i] - (location[i+1] - location[i]))))

        O(2^n) Time complexity
        O(len(stations)) for space recursive stack

        Idea: pq (maxHeap) store fuel at station
        [60, 30, 30]
        when we run out of fuel, backtrack to see if we could have pick up fuel to make it to current location

        [[10,60],[20,30],[target(100), float('inf')]]
                            i
        stops = 2
        tank = startFuel = -40
        pq = [] => if not more elemenets and tank < 0: not possible to reach destination

        Time: O(n)
        Space: O(n)

        '''

        pq = []
        stops = 0
        tank = startFuel
        prevLocation = 0

        stations.append([target, 100000])

        for location, fuel in stations:
            tank -= (location-prevLocation)
            while tank < 0 and pq:
                tank += -heapq.heappop(pq)
                stops += 1
            # Ran out of stations in our pq
            if tank < 0:
                return -1 # no way to reach destination
            heapq.heappush(pq, -fuel)
            prevLocation = location

        return stops


        '''
        Edge Case empty stations ex destination 100, startfueld is 0
        target = 100, startFuel = 10, 
        stations = [[10,60],[20,30],[30,30],[60,40], [100]]
                                            i
        pq = [ 30, 30]
        stops = 1
        prevLocati0n = 20
        tank = 40

        '''

        