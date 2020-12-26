class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.backtrack(i,j,word):
                    return True
        return False
    
    def backtrack(self,row,col,suffix):
        if len(suffix)==0:
            return True
        if row<0 or row==self.ROWS or col<0 or col==self.COLS or self.board[row][col]!=suffix[0]:
            return False
        
        self.board[row][col]='#'
        for newRow,newCol in [(0,1),(0,-1),(1,0),(-1,0)]:
            if self.backtrack(row+newRow,col+newCol,suffix[1:]):
                return True
        self.board[row][col] = suffix[0]
        return False
        
        
