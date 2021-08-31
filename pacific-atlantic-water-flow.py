class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        m, n = len(heights), len(heights[0])
        vp, va = set(), set()
        p, a = [], []
        
        for r in range(m):
            p.append([r,0])
            a.append([r,n-1])
            
        for c in range(n):
            p.append([0,c])
            a.append([m-1,c])
            
        def dfs(r, c, visited):
            visited.add((r,c))
            
            dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]
            for dr, dj in dirs:
                newR, newC = r+dr, c+dj
                if (0 <= newR < m) and (0 <= newC < n) and ((newR, newC) not in visited) and (heights[r][c] <= heights[newR][newC]):
                    dfs(newR,newC, visited)
                    
        for r,c in p: 
            dfs(r, c, vp)
            
        for r,c in a:
            dfs(r, c, va)
            
        return va & vp
    
    
    
    
            
