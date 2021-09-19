class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        graph = collections.defaultdict(set)
        em_to_name = collections.defaultdict()
        
        for acc in accounts:
            name = acc[0]
            
            for em in acc[1:]:
                graph[em].add(acc[1])
                graph[acc[1]].add(em)
                em_to_name[em] = name
                
        
        visited = set()
        output = []
        
        for node in graph:
            if node not in visited:
                stack = collections.deque()
                subGraph = []
                stack.append(node)
                visited.add(node)
                
                while stack:
                    cur = stack.pop()
                    subGraph.append(cur)
                    
                    for u in graph[cur]:
                        if u not in visited:
                            stack.append(u)
                            visited.add(u)
                            
                output.append([em_to_name[node]] + sorted(subGraph))
                
        return output
                            
                            
                            
                            
                            
                            
                            
