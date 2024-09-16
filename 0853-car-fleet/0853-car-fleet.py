class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        input: target: int, position: int[], speed: int[]
        output: int (fleets)

        can car have speed <= 0? => No

        Intuion: Calculate time each car takes to reach target and seem how many cross at same time baseed on starting order of cars

        arget = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

        Car = (position, speed)
        Sort by position and iterate backwards
        Time to reach finish is (target-position) / speed
        Only need to maintain eta of car at top of fleet in stack
        lenght of stack are how many different fleets are created

        [(0,1), (3, 3), (5,1), (8, 4), (10, 2)]
            i

        stack = [1.0, 7.0, 12]

        if stack and stack[-1] >= curEta:
            continue
        else:
            stack.append(curEta)

        
        Time: O(NlogN) to sort cars
        Space: O(N) for stack
        '''

        cars = [(p,s) for p, s in zip(position, speed)]
        stack = []

        for p, s in reversed(sorted(cars)):
            eta = (target - p) / s
            if stack and stack[-1] >= eta:
                continue
            else:
                stack.append(eta)
        return len(stack)

        