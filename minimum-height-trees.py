class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # edge cases
        if n <= 2:
            return [i for i in range(n)]
        graph = collections.defaultdict(list)
        in_degree = [0 for _ in range(n)]
        
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
            in_degree[v1] += 1
            in_degree[v2] += 1
            
        q = collections.deque()
        remainingNodes = n
        
        for i in range(n):
            if in_degree[i] == 1:
                q.append(i)
        while remainingNodes > 2:
            remainingNodes -= len(q)
            for _ in range(len(q)):
