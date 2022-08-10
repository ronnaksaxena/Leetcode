class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        rows, cols = len(points), len(points[0])
        # To cache max points for every cell in current row
        dp = points[0]
        # To store max point value found from left and right
        left, right = [0] * cols, [0] * cols
        
        for i in range(1, rows):
            # Find max points derived from r-1
            # Forward pass to find left points above and to left of point
            for j in range(cols):
                if j == 0:
                    left[j] = dp[j] # no points to left
                else:
                    left[j] = max(left[j-1]-1, dp[j])
                
            # Reverse pass to find right points above and right of point
            for j in range(cols-1,-1,-1):
                if j == cols-1:
                    right[j] = dp[j]
                else:
                    right[j] = max(right[j+1]-1, dp[j])
            
            # Calulcate max points path for row i
            for j in range(cols):
                dp[j] = max(left[j],right[j]) + points[i][j]
                
        return max(dp)
            
        
