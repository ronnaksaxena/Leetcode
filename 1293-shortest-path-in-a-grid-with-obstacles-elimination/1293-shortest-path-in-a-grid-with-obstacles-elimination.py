class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        target = (m-1, n-1)
        best = {} # (r,c): lives

        q = collections.deque([(0, 0, k)]) # row, col, removals left

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        depth = 0
        while q:
            for _ in range(len(q)):
                curR, curC, livesLeft = q.popleft()

                if (curR, curC) == target:
                    return depth

                if grid[curR][curC] == 1:
                    livesLeft -= 1

                if livesLeft >= 0:
                    for dR, dC in dirs:
                        newR, newC = curR + dR, curC + dC
                        if 0 <= newR < m and 0 <= newC < n and livesLeft > best.get((newR,newC), float('-inf')):
                            best[(newR, newC)] = livesLeft
                            q.append((newR, newC, livesLeft))

            depth += 1

        return -1 # no path found

        