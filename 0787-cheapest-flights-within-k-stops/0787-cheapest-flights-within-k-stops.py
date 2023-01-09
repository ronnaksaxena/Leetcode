class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        minDist = [float('inf') for _ in range(n)]
        minDist[src] = 0
        
        for _ in range(k+1):
            temp = copy.deepcopy(minDist)
            for start, end, price in flights:
                if minDist[start] + price < temp[end]:
                    temp[end] = minDist[start] + price
            minDist = temp
            
        return minDist[dst] if minDist[dst] != float('inf') else -1
                
            
        
        