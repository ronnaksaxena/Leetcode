class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        return len(set(count.values())) == len(count.keys())
        