class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        ans = []
        n, m = len(mat), len(mat[0])
        heap = []
        for i in range(n):
            ones = 0
            for j in range(m):
                ones += mat[i][j]
            heapq.heappush(heap, (ones,i))
            
        while k:
            _,row = heapq.heappop(heap)
            k -= 1
            ans.append(row)
            
        return ans
