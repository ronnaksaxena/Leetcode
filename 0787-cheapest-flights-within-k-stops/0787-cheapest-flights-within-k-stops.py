class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        minPrices = [float('inf') for _ in range(n)]
        minPrices[src] = 0
        
        # Do k stops
        for _ in range(k+1):
            temp = minPrices[:]
            # Bellman Ford
            for start, end, price in flights:
                if minPrices[start] + price < temp[end]:
                    temp[end] = minPrices[start] + price
            minPrices = temp
            
        return minPrices[dst] if minPrices[dst] != float('inf') else -1
        