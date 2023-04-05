class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Make adj list
        graph = collections.defaultdict(list)
        in_degree = [0 for _ in range(numCourses)]
        for post, pre in prerequisites:
            graph[pre].append(post)
            in_degree[post] += 1
        
        # q for Kahn's top sort
        q = collections.deque()
        for i in range(len(in_degree)):
            if not in_degree[i]:
                q.append(i)
        order = []
        while q:
            cur = q.popleft()
            order.append(cur)
            for nei in graph[cur]:
                in_degree[nei] -= 1
                if not in_degree[nei]:
                    q.append(nei)
        return len(order) == numCourses
        
        