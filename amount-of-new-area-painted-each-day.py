class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        # Cache painted intervals
        # painted i : last index
        painted = {}
        output = []
        
        for start, end in paint:
            curPaint = start
            curArea = 0
            while curPaint < end:
                # Check if section painted already
                if curPaint in painted:
                    # Make sure upper bound is max value painted
                    # ex. 4 => 7 can be optimized to 4 => 9
                    # Change curPaint to painted section's end value
                    painted[curPaint], curPaint = max(end, painted[curPaint]), painted[curPaint]
                    
                else:
                    curArea += 1
                    painted[curPaint] = end
                    curPaint += 1
            output.append(curArea)
            
        return output
            
        
            
