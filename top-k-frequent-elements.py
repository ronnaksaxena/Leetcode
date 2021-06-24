class Solution:
    import collections
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        return heapq.nlargest(k, freq.keys(), key=freq.get)
