class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        '''
        Brute force traverse top & left border and check for same elements
        O(N)
        
        Optimal:Check every top left neighbor
        
        Time: O(N)
        Sapce: O(1)
        
        loop r & c througth matrix
            if r-1 >= 0 and c -1 >= 0 and matrix[r-1][c-1] != matrix[r][c]:
                return False
        
        return True
        
        '''
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r -1 >= 0 and c - 1 >= 0 and matrix[r-1][c-1] != matrix[r][c]:
                    return False
        return True
        