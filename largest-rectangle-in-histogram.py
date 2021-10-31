class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [-1]
        maxArea = 0
        
        for i in range(len(heights)):
            
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                curHeight = heights[stack.pop()]
                curWidth = i - stack[-1] - 1
                curArea = curWidth * curHeight
                maxArea = max(maxArea, curArea)
                
            stack.append(i)
            
        
        while stack[-1] != -1:
            curHeight = heights[stack.pop()]
            curWidth = len(heights) - stack[-1] - 1
            curArea = curWidth * curHeight
            maxArea = max(maxArea, curArea)
            
        return maxArea
        
        
