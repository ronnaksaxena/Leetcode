class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:

        m, n = len(mat), len(mat[0])
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((mat[i][j], i, j))

        # Sort cells by their values in ascending order
        cells.sort(key=lambda x: x[0])

        row_max = defaultdict(int)
        col_max = defaultdict(int)
        dp = {}
        max_cells = 1

        # We'll group cells by their value
        i = 0
        while i < len(cells):
            value = cells[i][0]
            # Collect all cells with this value
            group = []
            while i < len(cells) and cells[i][0] == value:
                group.append(cells[i])
                i += 1

            # First phase: compute dp for all cells of this value (do not update row/col max yet)
            temp_updates = []
            for val, r, c in group:
                dp[(r, c)] = 1 + max(row_max[r], col_max[c])
                max_cells = max(max_cells, dp[(r, c)])
                temp_updates.append((r, c, dp[(r, c)]))

            # Second phase: after computing all dp for this value, now update row_max and col_max
            for r, c, d in temp_updates:
                row_max[r] = max(row_max[r], d)
                col_max[c] = max(col_max[c], d)

        return max_cells


        