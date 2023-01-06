class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list) # node : [(distance, neighbor)]
        
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i].append((distance, j))
                graph[j].append((distance, i))
                
        minCost = 0
        totalPoints = len(points)
        heap = [(0, 0)]
        visited = set()
        
        while heap and totalPoints > 0:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            minCost += cost
            totalPoints -= 1
            visited.add(node)
            for dist, nei in graph[node]:
                if nei not in visited:
                    heapq.heappush(heap, (dist, nei))
        
        return minCost
                
                
                
                
                
        