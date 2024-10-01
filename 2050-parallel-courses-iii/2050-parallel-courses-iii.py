class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        '''

        1 -> 
            2 -> 3
        4 ->

        TimeNeeded[3] = max(prevCourses[2]) + time[2]
        '''

        graph = collections.defaultdict(list)
        inDegree = {i: 0 for i in range(1, n+1)}
        time = {course: t for course, t in enumerate(time,1)}

        for prev, post in relations:
            graph[prev].append(post)
            inDegree[post] += 1

        q = collections.deque()
        maxTimes = {i: 0 for i in range(1, n+1)}
        for course, deg in inDegree.items():
            if not deg:
                q.append(course)
                maxTimes[course] = time[course]
        
        while q:
            curCourse = q.popleft()
            for nextCourse in graph[curCourse]:
                maxTimes[nextCourse] = max(maxTimes[nextCourse], time[nextCourse] + maxTimes[curCourse])
                inDegree[nextCourse] -= 1
                if not inDegree[nextCourse]:
                    q.append(nextCourse)
        return max(maxTimes.values())
        