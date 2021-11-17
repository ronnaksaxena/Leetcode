class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        #possible moves are (-1,2),(-2,1),(1,2),(2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)
        
        
        level = -1
        visited = set()
        q = collections.deque()
        q.append((0,0))
        visited.add((0,0))
        dirs = [(-1,2),(-2,1),(1,2),(2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        
        while q:
            level += 1
            
            for _ in range(len(q)):
                curX, curY = q.popleft()
                
                if curX == x and curY == y:
                    return level
                
                for dX, dY in dirs:
                    newX, newY = curX + dX, curY + dY
                    
                    if (newX,newY) not in visited:
                        visited.add((newX,newY))
                        q.append((newX,newY))
                        
        return -1
                
