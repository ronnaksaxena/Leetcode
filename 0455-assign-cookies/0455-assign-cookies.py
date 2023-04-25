class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        count = 0
        heapq.heapify(s)
        
        for child in g:
            while s and s[0] < child:
                heapq.heappop(s)
            if not s:
                break
            heapq.heappop(s)
            count += 1
        return count
                
        