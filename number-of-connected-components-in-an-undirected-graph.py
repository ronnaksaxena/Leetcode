class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = {i:[] for i in range(n)}
        
        for a,b in edges:
            adjList[a] += [b]
            adjList[b] += [a]
            
        count = 0
        visited = set()
        for i in range(n):
            if not i in visited:
                count += 1
                q = collections.deque()
                q.append(i)
                while q:
                    cur = q.popleft()
                    for u in adjList[cur]:
                        if not u in visited:
                            q.append(u)
                    visited.add(cur)
        return count
                    
