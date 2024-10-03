class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # Sorting tickets puts [fromi, toi] in order for selections
        tickets.sort()
        graph = collections.defaultdict(list)
        # Will have Vs in adjList in sorted order
        for src, sink in tickets:
            graph[src].append(sink)
        
        path = ['JFK']
        def dfs(cur):
            nonlocal path
            # All flights taken + 1 for first stop at JFK
            if len(path) == len(tickets) + 1:
                return True
            # No more paths to explore
            if not graph[cur]:
                return False
            # To change adjList while iterating
            temp = graph[cur].copy()
            for i,v in enumerate(temp):
                graph[cur].pop(i)
                path.append(v)
                # Backtrack until path found
                if dfs(v): return True
                graph[cur].insert(i,v)
                path.pop()
            
            return False
        dfs('JFK')
        return path
            
            
        
        
            
        