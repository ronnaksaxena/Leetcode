class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        '''
        - rectangle matrix
        - can be duplicate values
        - flip order of each diagonal
        
        
        [1,2,3, 10]
        [4,5,6, 11]
        [7,8,9, 12]
        
        0 + 0 => 0 : [1]
        0 + 1, 1 + 0 => 1 [2, 4]
        2 + 0, 1 + 1, 0 + 2 => 2 [3, 5, 7]
        2 + 1, 2 + 1 => 3 [6,8]
        2 + 2 => 4 [9]
        
        diagonal idx == r + c
        idea: hashmap {diagonal index: [elements in that diagonal]}
        
        if diagonal index is even: reverse order of elements that were added
        
        - Traverse matrix
            - add element to hashmap based on diagonal index
        - Traverse map by diagonal index
            - if diagonal index is even: reverse order of elements in that map
        Time: O(m x n) where m is rows and n is colums
        Space: O(m x n) to store all values in map
        
        '''
        diagonals = collections.defaultdict(list) # {diagonal index: [elements]}
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                diagonals[r+c].append(mat[r][c])
        output = []
        for dIndex in sorted(diagonals.keys()):
            if dIndex % 2:
                output.extend(diagonals[dIndex])
            else:
                # Reverse even diagonals
                
                output.extend(diagonals[dIndex][::-1])
        return output
        
        
        