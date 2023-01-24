class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        totalCells = len(board) * len(board[0])
        ROWS, COLS = len(board), len(board[0])
        # Returns the board index of the cell
        def findIndex(cell):
            nonlocal ROWS
            nonlocal COLS
            row = (ROWS-1) - ((cell-1) // COLS)
            # Increasing row if even, decreasing if odd, 0-indexed
            col = (cell-1)%COLS if (ROWS-1-row) % 2 == 0 else (COLS-1) - (cell-1)%COLS
            return [row, col]
        
        destination = totalCells
        visited = {1}  # cell
        q = collections.deque([(1, 0)])  # (cell, moves)
        # BFS
        while q:
            cell, moves = q.popleft()
            if cell == destination:
                return moves
            for roll in range(1,7):
                nextCell = cell + roll
                if nextCell <= destination:
                    nextRow, nextCol = findIndex(nextCell)
                    if board[nextRow][nextCol] != -1:
                        nextCell = board[nextRow][nextCol] if nextCell != destination else nextCell
                    if nextCell not in visited:
                        q.append((nextCell, moves+1))
                        visited.add(nextCell)
                    
        return -1
                    
        
                
        