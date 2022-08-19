class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Construct AdjList
        graph = collections.defaultdict(list)
        for src, sink in edges:
            graph[src].append(sink)
        # Colors: WHITE = Not processed yet, GREY = processing, BLACK = done
        # Can omit visited sets for coloring method
        colors = {i : 'w' for i in range(n)}
        
        def leadsToDest(node):
            # if had no neighbors must be destination
            if len(graph[node]) == 0:
                return node == destination
            # Check if cycle found
            if colors[node] != 'w':
                # If grey theres a cycle
                return colors[node] == 'b'
            # Mark as processing
            colors[node] = 'g'
            
            for neighbor in graph[node]:
                if not leadsToDest(neighbor):
                    return False
            # Mark as finished processing
            colors[node] = 'b'
            return True
        
        return leadsToDest(source)
            
                    
            
            
            
            
    
    
    
    '''
    Conditions:
    1. Node is destination : return True
