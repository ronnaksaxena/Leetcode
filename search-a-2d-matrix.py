class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        L, R = 0, (n*m)-1
        while L<=R:
            mid = L+(R-L)//2
            val = matrix[mid//n][mid%n]
            if val==target:
                return True
            elif val>target:
                R = mid-1
            else:
                L = mid+1
        return False
            
                
