class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Start from both ocean borders and see which can flow into both
        pSet = set()
        aSet = set()
        
        rows, cols = len(heights), len(heights[0])
        
        # Add left and right squares to sets
        for r in range(rows):
            pSet.add((r,0))
            aSet.add((r, cols-1))
        # Add top and bottom squares to sets
        for c in range(cols):
            pSet.add((0, c))
            aSet.add((rows-1, c))
        
        # BFS on Atlantic squares
        q = collections.deque(list(aSet))
        while q:
            curR, curC = q.popleft()
            for dR, dC in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newR, newC = curR + dR, curC + dC
                if 0 <= newR < rows and 0 <= newC < cols and (newR, newC) not in aSet and heights[newR][newC] >= heights[curR][curC]:
                    aSet.add((newR, newC))
                    q.append((newR, newC))
        # BFS in Pacific squares
        q = collections.deque(list(pSet))
        while q:
            curR, curC = q.popleft()
            for dR, dC in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newR, newC = curR + dR, curC + dC
                if 0 <= newR < rows and 0 <= newC < cols and (newR, newC) not in pSet and heights[newR][newC] >= heights[curR][curC]:
                    pSet.add((newR, newC))
                    q.append((newR, newC))
        return aSet & pSet
        
                
        