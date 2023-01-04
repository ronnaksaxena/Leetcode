class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = collections.Counter(tasks)
        # max heap
        heap = []
        for val, freq in count.items():
            heapq.heappush(heap, (-freq, val))
        rounds = 0
        needToComplete = len(tasks)
        
        while needToComplete > 0:
            rounds += 1
            maxCount, val = heapq.heappop(heap)
            maxCount *= -1
            if maxCount == 1:
                return -1 # Not possible
            if maxCount % 3 == 0:
                maxCount -= 3
                needToComplete -= 3
                heapq.heappush(heap, (-maxCount, val))
            else:
                maxCount -= 2
                needToComplete -= 2
                heapq.heappush(heap, (-maxCount, val))
        return rounds
            
        