class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0] * n

        # {prevCourse: [nextCourses]}
        graph = collections.defaultdict(list)

        for prev, nextCourse in relations:
            graph[prev-1].append(nextCourse-1)
            indegree[nextCourse-1] += 1
        
        max_time = [0] * n
        q = collections.deque()
        for course in range(n):
            if indegree[course] == 0:
                q.append(course)
                max_time[course] = time[course]
        
        # Kahns
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                max_time[neighbor] = max(max_time[neighbor], max_time[node] + time[neighbor])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return max(max_time)

        