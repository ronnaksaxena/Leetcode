class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = collections.Counter(arr)
        n = len(arr)
        return [x for x in count.keys() if count[x] / n > 0.25][0]
        