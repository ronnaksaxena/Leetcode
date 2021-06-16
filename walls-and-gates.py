class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    q = collections.deque()
                    visited = set()
​
                    q.appendleft((i+1,j,1))
​
                    q.appendleft((i-1,j,1))
​
                    q.appendleft((i,j+1,1))
​
                    q.appendleft((i,j-1,1))
                    while q:
                        row, col, val = q.popleft()
                        if (0 <= row < m) and (0 <= col < n) and not (row,col) in visited and rooms[row][col] > 0:
                            rooms[row][col] = min(rooms[row][col], val)
                            q.append((row+1,col,val+1))
                            q.append((row-1,col,val+1))
                            q.append((row,col+1,val+1))
                            q.append((row,col-1,val+1))
                            visited.add((row,col))
                        
        return
                        
                            
                            
                            
                            
                            
