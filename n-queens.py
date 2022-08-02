class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # cached sets
        cols = set()
        posDiags = set() # (r + c)
        negDiags = set() # (r - c)
        board = [['.'] * n for _ in range(n)]
        output = []
        
        # Can only place 1 queen per row
        def dfs(r):
            # Found board solution
            if r == n:
                copy = [''.join(row) for row in board]
                output.append(copy)
                return
​
            # Look for possible cols
            for c in range(n):
                if c not in cols and (r+c) not in posDiags and (r-c) not in negDiags:
                    # Place Q and search next row
                    cols.add(c)
                    posDiags.add(r+c)
                    negDiags.add(r-c)
                    board[r][c] = 'Q'
                    dfs(r+1)
                    # Backtrack
                    cols.remove(c)
                    posDiags.remove(r+c)
                    negDiags.remove(r-c)
                    board[r][c] = '.'
                        
        dfs(0)
        return output
                    
        
