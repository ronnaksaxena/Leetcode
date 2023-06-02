class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def getDistance(x1, y1, x2, y2):
            return sqrt(((x1-x2)**2) + ((y1-y2)**2))
        longestChain = 0
        n = len(bombs)
        # Create graph
        graph = collections.defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue # skip same bomb
                xi, yi, ri = bombs[i]
                xj, yj, rj = bombs[j]
                distance = getDistance(xi, yi, xj, yj)
                # i would detonate j
                if ri >= distance:
                    graph[i].append(j)
        def bfs(i):
            q = collections.deque([i])
            visited = {i}
            curChain = 0
            while q:
                cur = q.popleft()
                curChain += 1
                for nei in graph[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            return curChain
        # BFS to find longest path
        for i in range(n):
            longestChain = max(longestChain, bfs(i))
                
        return longestChain
                
        