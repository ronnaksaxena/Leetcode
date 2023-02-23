class Solution:
    def maxScore(self, A: List[int], B: List[int], k: int) -> int:
        total = res = 0
        h = [] # min heap to kick out lowest element in subsequence
        scores = list(zip(A, B))
        # sorted max -> min values of B
        scores.sort(key=lambda x: -x[1])
        res = float('-inf')
        total = 0 # sum of current subsequence
        for a, b in scores:
            total += a
            heapq.heappush(h, a)
            if len(h) > k:
                total -= heapq.heappop(h)
            if len(h) == k:
                res = max(res, total * b)
        return res
            
            
        