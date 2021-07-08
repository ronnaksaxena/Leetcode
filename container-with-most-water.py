class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea, L, R = 0, 0, len(height)-1
        
        while L < R:
            area = (R-L) * min(height[R],height[L])
            maxArea = max(maxArea, area)
            if height[R] < height[L]:
                R -= 1
            else:
                L += 1
        
        return maxArea
        
