class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        netShifts = 0
        
        for d,n in shift:
            if d == 0:
                netShifts -= n
            else:
                netShifts += n
        print(netShifts)
                
        if netShifts == 0:
            return s
        
        if netShifts < 0:
            numShifts = abs(netShifts)%len(s)
            return s[numShifts:] + s[:numShifts]
        else:
            numShifts = abs(netShifts)%len(s)
            return s[(numShifts*-1):] + s[:-numShifts]
