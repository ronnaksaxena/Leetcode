class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([c*f for c,f in sorted(collections.Counter(s).items(), key = lambda x: x[1], reverse=True)])
        