class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        height = 0
        pointsRight = False
        goingUp = True
        
        while True:
            if goingUp:
                if height+q <= p:
                    height += q
                    pointsRight = not pointsRight
                else:
                    height = p - ((height+q)%p)
                    pointsRight = not pointsRight
                    goingUp = False
            else:
                if height-q >= 0:
                    height -= q
                    pointsRight = not pointsRight
                else:
                    height = abs(height-q)
                    pointsRight = not pointsRight
                    goingUp = True
                    
            if height == 0 and pointsRight:
                return 0
            if height == p and pointsRight:
                return 1
            if height == p and not pointsRight:
                return 2
        
        
        
