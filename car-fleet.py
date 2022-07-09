class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [(p,s) for p,s in zip(position,speed)]
        
        stack = []
        
        #want to iteratre through cars from right to left
        for p,s in reversed(sorted(cars)):
            #float division since eta can be a decimal
            eta = (target-p) / s
            stack.append(eta)
            
            #only update fleets if 2 or more cars
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        
        return len(stack)
