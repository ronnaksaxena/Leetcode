class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # If we can created top sort with all courses it is possible
        in_degree = [0 for _ in range(numCourses)]
        graph = collections.defaultdict(list)

        for post, pre in prerequisites:
            in_degree[post] += 1
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
        
        return order if len(order) == numCourses else []