class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        if not m or not n:
            return 0
        cache = [[0 for _ in range(n)] for _ in range(m)]
        maxLen = 0
        
        for i in range(m):
            for j in range(n):
                path = self.DFS(i,j,cache, matrix)
                maxLen = max(path, maxLen)
        
        return maxLen
    
    def DFS(self,row, col, cache, matrix):
        if cache[row][col] > 0:
            return cache[row][col]       
        m, n = len(matrix), len(matrix[0])
        maxPath = 0
        offSets = [(1,0), (-1,0), (0, 1), (0,-1)]
        for newRow,newCol in offSets:
            if 0 <= row+newRow < m and 0 <= col+newCol < n and matrix[row][col] < matrix[row+newRow][col+newCol]:
                path = self.DFS(row+newRow,col+newCol,cache,matrix)
                maxPath = max(maxPath, path)
        
        cache[row][col] = maxPath + 1
        
        return cache[row][col]
