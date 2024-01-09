class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = [] # Max heap of k smallest points
        
        for x, y in points:
            eDist = sqrt(x**2 + y**2)
            if len(heap) == k:
                if abs(heap[0][0]) > eDist:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-eDist, x, y))
            else:
                heapq.heappush(heap, (-eDist, x, y))
                
        ans = []
        while heap:
            _, x, y = heapq.heappop(heap)
            ans.append([x,y])
        return ans
                
        