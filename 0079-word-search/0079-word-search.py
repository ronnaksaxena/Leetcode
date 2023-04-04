class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        DFS but don't give up on a path if the search doesn't yield the word
            have to pop from visited or unmark baord
        
        ["A","B","C","E"]
        ["S","F","C","S"]
        ["A","D","E","E"]
        
        word = 'ABCCED'
        pre = 'ABCCED'
        
        '''
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, word):
            # Found word
            if not word:
                return True
            # Not valid path
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[0]:
                return False
            # mark as visited
            oldLetter = board[r][c]
            board[r][c] = '#'
            for dR, dC in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newR, newC = r+dR, c+dC
                if dfs(newR, newC, word[1:]):
                    return True
            # Backtrack back to old spot
            board[r][c] = oldLetter
            return False
                
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, word):
                        return True
        return False