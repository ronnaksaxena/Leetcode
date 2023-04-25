class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n = len(workers)
        output = [None for _ in range(n)]
        # to get closest bike paris
        pq = []
        # populate with remaining bike pairs
        workerBikePairs = []
        
        # PQ with (distance, worker idx, bike idx)
        distances = []
        for wI, (wX, wY) in enumerate(workers):
            curPairs = []
            for bI, (bX, bY) in enumerate(bikes):
                d = abs(bX-wX) + abs(bY-wY)
                curPairs.append((d, wI, bI))
            curPairs.sort(reverse=True)
            heapq.heappush(pq, curPairs.pop())
            workerBikePairs.append(curPairs)
        # seen for bikes
        seenBikes = set()
        while pq:
            _, worker, bike = heapq.heappop(pq)
            # Found free bike
            if bike not in seenBikes:
                output[worker] = bike
                seenBikes.add(bike)
            # Need to get next bike
            else:
                _, _, nextClosest = workerBikePairs[worker].pop()
                wX, wY = workers[worker]
                bX, bY = bikes[nextClosest]
                d = abs(bX-wX) + abs(bY-wY)
                heapq.heappush(pq, (d, worker, nextClosest))
        
            
        return output
        