class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowestRow = 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][0]< target:
                lowestRow = i
                break
        for i in range(lowestRow,m):
            L, R = 0, n-1
            while L<=R:
                mid = L + (R-L)//2
                val = matrix[i][mid]
                if val==target:
                    return True
                elif val>target:
                    R = mid-1
                else:
                    L = mid+1
        return False
        
