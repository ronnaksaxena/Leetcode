class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # If we can created top sort with all courses it is possible
        in_degree = [0 for _ in range(numCourses)]
        graph = collections.defaultdict(list)

        for post, pre in prerequisites:
            in_degree[post] += 1
            if pre not in in_degree:
                in_degree[pre] = 0
            graph[pre].append(post)
        
        q = collections.deque()
        for course, deg in enumerate(in_degree):
            if not deg:
                q.append(course)
        
        order = []
        while q:
            cur = q.popleft()
            order.append(cur)

            for post in graph[cur]:
                in_degree[post] -= 1
                if not in_degree[post]:
                    q.append(post)
        
        return len(order) == numCourses

        