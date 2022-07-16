class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        mark all O's in path as E to ignore and continue DFS on rest of grid
        second iter: mark all O's as X
        
        '''
        rows, cols = len(board), len(board[0])
        #helper for capturing all non surrounded regions
        def capture(i, j):
            if 0 > i or 0 > j or i == rows or j == cols or board[i][j] != 'O':
                return
            board[i][j] = 'T'
            capture(i+1,j)
            capture(i-1,j)
            capture(i,j+1)
            capture(i,j-1)
            
        
        # 1. Capture all nonsurrounded regions O -> T
        for i in range(rows):
            for j in range(cols):
                #touches boarder so not surrounding
                if i in [0, rows-1] or j in [0, cols-1]:
                    #DFS on all neighbors
                    capture(i,j)
        # 2. All remainig O's are surrounded O -> X
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                
        # 3. Set all nonsurrounded regions back to O T -> O
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                    
                        
                        
                        
                        
                        
                        
                        
                        
