class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        [5,10,-5]
         i
        stack = [5]
        
        while len(stack) >= 2 and isColliding(stack[-1], stack[-2]):
            a1, a2 = stack.pop(), stack.pop()
            if abs(a1) > abs(a2):
                stack push a1
            elif abs(a2) > abs(a1):
                stack push a2
            # Otherwise both explode
        
        algo:
        1. loop through asteroids
        2. push to stack
        3. compute collisions
        4. return stack
        
        '''
        def isColliding(leftA, rightA):
            return (leftA > 0 and rightA < 0)
        stack = []
        for a in asteroids:
            stack.append(a)
            while len(stack) >= 2 and isColliding(stack[-2], stack[-1]):
                a1, a2 = stack.pop(), stack.pop()
                if abs(a1) > abs(a2):
                    stack.append(a1)
                elif abs(a2) > abs(a1):
                    stack.append(a2)
        return stack
                
        
        