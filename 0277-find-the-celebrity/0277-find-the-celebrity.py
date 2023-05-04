# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        cand = 0
        
        # Find possible celeb candidate
        for i in range(1, n):
            if knows(cand, i):
                cand = i
        # Verify it is a celeb
        for i in range(0, n):
            if i == cand:
                continue
            if knows(cand, i) or not knows(i, cand):
                return -1
        return cand
            
        