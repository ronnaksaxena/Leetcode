class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = collections.defaultdict(list)
        ROWS, COLS = len(mat), len(mat[0])
        for r in range(ROWS):
            for c in range(COLS):
                # All elements that share a sum of r and c are in same diagonal
                diagonals[r+c].append(mat[r][c])
        output = []
        # Build diagonal traversal
        for d in sorted(diagonals.keys()):
            # If even diagonal reverse elements order
            if d % 2 == 0:
                output.extend(diagonals[d][::-1])
            else:
                output.extend(diagonals[d])
        return output
                
        