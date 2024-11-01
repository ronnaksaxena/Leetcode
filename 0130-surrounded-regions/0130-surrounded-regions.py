class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        def bfs(r, c):
            # Mark all safe coordinates as 'Y'
            q = collections.deque([(r,c)])
            d = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            while q:
                curR, curC = q.popleft()
                for dR, dC in d:
                    newR, newC = curR+dR, curC+dC
                    if 0 <= newR < rows and 0 <= newC < cols and board[newR][newC] == 'O':
                        q.append((newR, newC))
                        board[newR][newC] = 'Y'
            return
        
        # Find all non surrounded regions and mark at Y
        for r in range(rows):
            if board[r][0] == 'O':
                board[r][0] = 'Y'
                bfs(r,0)
            if board[r][cols-1] == 'O':
                board[r][cols-1] = 'Y'
                bfs(r, cols-1)

        for c in range(cols):
            if board[0][c] == 'O':
                board[0][c] = 'Y'
                bfs(0, c)
            if board[rows-1][c] == 'O':
                board[rows-1][c] = 'Y'
                bfs(rows-1, c)

        # All remaining Os are marked to X and all remaining Ys marked to O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'Y':
                    board[r][c] = 'O'

        return

        