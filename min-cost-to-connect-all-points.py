class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # i : [(cost), neighbors]
        graph = collections.defaultdict(list)
        # Nodes in points
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                X1,Y1 = points[i][0], points[i][1]
                X2,Y2 = points[j][0], points[j][1]
                # 1 : (Manhattan distance between p1 and p2, 2)
                dist = abs(X1-X2) + abs(Y1-Y2)
                graph[i].append((dist, j))
                # Same for neighbors since undirected graph
                graph[j].append((dist, i))
                
        heap = [(0,0)]
        cost = 0
        visited = set()
        # Iterate until we visited every node
        while len(visited) < n:
            curCost, curNode = heapq.heappop(heap)
            # Check that node was not visited yet
            if curNode in visited: continue
            # Fres node
            cost += curCost
            visited.add(curNode)
            for uCost, u in graph[curNode]:
                if u not in visited:
                    heapq.heappush(heap, (uCost, u))
                    
        return cost
        
        
