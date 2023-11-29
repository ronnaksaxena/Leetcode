class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = [] # max heap (frequency, word)
        cnt = collections.Counter(words)
        for w, freq in cnt.items():
            heapq.heappush(heap, (-freq, w))
        return [heapq.heappop(heap)[1] for _ in range(k)]
        
        