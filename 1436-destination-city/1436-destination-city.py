class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        inDegree = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        for a,b in paths:
            inDegree[b] += 1
            graph[a].append(b)
        q = collections.deque()
        for city in graph.keys():
            if not inDegree[city]:
                q.append(city)
        topOrder = []
        while q:
            cur = q.popleft()
            topOrder.append(cur)
            for nei in graph[cur]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)
        return topOrder[-1]