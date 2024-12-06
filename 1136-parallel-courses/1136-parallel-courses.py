class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        '''
        Clarifications:

        - intput: int, [[int,int]] => output int
        - 1 semester per class
        - 1 -> 2 -> 1 == can be cycle
        - n == 100 [] => possible for no pre reqs

        n = 3, relations = [[1,3],[2,3]]

        1       2
          \.   /
            3

            output 2 since sem 1 (1,2) sem 2 (3)

        input n = 4, [1,4], [2,3], [3,4]

        1.   2 -> 1
        |.  /
        |   3. -> 2
        |. /
        4. -> 3

        output 3 sem (1,2) sem 2 (3) sem 3 (4)

        keep track of in_degree

        traverse by depth (semesters)
        if we can visit every node (class) there is an ordering

        1 ----> 2
        \.     /
            3

        all have an indgree of 1

        Algo:
        1. build graph + in degree

            {class: [post requisites]}
            in_degree = [class : num of edges pointed to it]

        2. init q & int var num of semesters

            [courses with no pre req]
            num of semesters = 0
            visited = set {courses}

        3. topological trav

            while q
                loop thorught lenght of q
                    add to set
                    check if we met pre reqs for next course
                        add next course to set
                inc num of semester

        4.
            if visited every course:
                return semesters
            else:
                -1

        time complexity: O(N + E) (courses + relationship)
        Space Complexity: O(N)

        '''

        graph = {course: [] for course in range(1,n+1)}
        inDegree = {course: 0 for course in range(1,n+1)}

        for pre, post in relations:
            graph[pre].append(post)
            inDegree[post] += 1

        q = collections.deque()
        # Start wtih courses with no pre reqs
        for course in range(1, n+1):
            if not inDegree[course]:
                q.append(course)

        courseVisited = set()
        semestersNeeded = 0

        # Top sort
        while q:
            # iterate thorugh all courses this semseter
            for _ in range(len(q)):
                curCourse = q.popleft()
                courseVisited.add(curCourse)

                for nextCourse in graph[curCourse]:
                    inDegree[nextCourse] -= 1
                    if inDegree[nextCourse] == 0:
                        q.append(nextCourse)

            semestersNeeded += 1

        return semestersNeeded if len(courseVisited) == n else -1

        