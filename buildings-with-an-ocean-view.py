class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        maxHeight = 0
        output = collections.deque()
        
        for i in range(len(heights)-1,-1,-1):
            if heights[i] > maxHeight:
                output.appendleft(i)
            
            maxHeight = max(maxHeight, heights[i])
            
        return output
                
        
