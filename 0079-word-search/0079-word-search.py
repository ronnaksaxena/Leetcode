class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        rows, cols = len(board), len(board[0])

        def backtrack(r, c, index):
            # Found the complete word
            if index == len(word):
                return True
            # Out of bounds or character mismatch
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False

            # Mark the cell as visited by temporarily changing the board character
            temp = board[r][c]
            board[r][c] = "#"

            # Explore neighbors in the four possible directions (up, down, left, right)
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if backtrack(new_r, new_c, index + 1):
                    return True

            # Restore the original character after backtracking
            board[r][c] = temp

            return False

        for r in range(rows):
            for c in range(cols):
                # Start the backtracking only if the first character matches
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True

        return False
