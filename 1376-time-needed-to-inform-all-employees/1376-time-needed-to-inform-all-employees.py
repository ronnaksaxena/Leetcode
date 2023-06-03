class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Make graph
        graph = collections.defaultdict(list)
        
        for worker in range(n):
            # manager -> worker
            graph[manager[worker]].append(worker)
        # Do a dfs on headID to find longest time
        def dfs(worker):
            # At leaf worker
            if not graph[worker]:
                return 0
            # find max time needed
            timeNeeded = float('-inf')
            for subordinate in graph[worker]:
                timeNeeded = max(timeNeeded, informTime[worker] + dfs(subordinate))
            return timeNeeded
        
        return dfs(headID)
        