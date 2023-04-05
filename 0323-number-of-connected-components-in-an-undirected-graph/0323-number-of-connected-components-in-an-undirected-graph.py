class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build undirected graph
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        componets = 0
        # BFS on all components
        for i in range(n):
            if i not in visited:
                componets += 1
                q = collections.deque([i])
                visited.add(i)
                while q:
                    cur = q.popleft()
                    for nei in graph[cur]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
                            
        return componets
                            
        