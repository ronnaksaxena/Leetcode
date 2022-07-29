class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        flightCost = {}
        
        # Initial cost from start is 0
        flightCost[src] = 0
        
        # BFS to find shortest path allowing K number of stops
        for _ in range(k+1):
            
            # Want to compare this iteration of K from last
            tempMap = flightCost.copy()
            for s, d, p in flights:
                # Found cheaper flight
                if tempMap.get(s,float('inf')) + p < flightCost.get(d, float('inf')):
                    flightCost[d] = tempMap[s] + p
            
        # Return cheapest path to dst if exists
        return flightCost[dst] if dst in flightCost else -1
        
