class Solution:
    def racecar(self, target: int) -> int:
        
        moves = 0
        q = collections.deque([(0, 1)]) # (position, speed)
        visited = {(0, 0)}
        # BFS
        while q:
            
            for _ in range(len(q)):
                position, speed = q.popleft()

                #check if reached target
                if position == target:
                    return moves
                #try to accelerate
                if (position+ speed, speed *2) not in visited:
                    q.append((position+speed, speed*2))
                    visited.add((position+speed,speed*2))

                #try to reverse under 2 conditions:
                #1: car is going foreward and you will pass target
                #2: car is going in reverse and is before target
                if (speed > 0 and position+speed > target) or (speed < 0 and position+speed < target):
                    #update speed according to conditions
                    speed = -1 if speed > 0 else 1
                    #do not change positions
                    if (position, speed) not in visited:
                        q.append((position,speed))
            moves += 1
            
        return -1
                