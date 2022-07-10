class Solution:
    def racecar(self, target: int) -> int:
        
        #queue holds (moves, position, speed)
        q = collections.deque([(0,0,1)])
        #hold visited nodes of (position, speed)
        visited = set()
        
        #BFS to find min num of moves
        while q:
            moves, position, speed = q.popleft()
            
            #check if reached target
            if position == target:
                return moves
            #already seen
            if (position, speed) in visited:
                continue
            
            visited.add((position,speed))
            
            #try to accelerate
            q.append((moves+1,position+speed, speed*2))
            
            #try to reverse under 2 conditions:
            #1: car is going foreward and you will pass target
            #2: car is going in reverse and is before target
            if (speed > 0 and position+speed > target) or (speed < 0 and position+speed < target):
                #update speed according to conditions
                speed = -1 if speed > 0 else 1
                #do not change positions
                q.append((moves+1,position,speed))
            
        
