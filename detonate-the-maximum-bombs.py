        
        # save bombs we already solved
        self.solved = {}
        
        # start at every bomb
        for idx in range(len(bombs)):
            
            # get the reachable bombs
            visited = set([idx])
            self.dfs(idx, visited, connections)
            
            # save the reachable bombs
            self.solved[idx] = visited
            
            # count reachable bombs
            self.max = max(self.max, len(visited))
            
        return self.max
    
    def dfs(self, current, visited, connections):
        
        # check if we already solved for this bomb
        if current in self.solved:
            # extend our path
            visited.update(self.solved[current])
            return
        
        # go deeper
        for idx in connections[current]:
            if idx not in visited:
                
                # update visited
                visited.add(idx)
