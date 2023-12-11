class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        candidates = [arr[n//4], arr[n//2], arr[3 * n // 4]]
        
        for c in candidates:
            l = bisect.bisect_left(arr, c)
            r = bisect.bisect_right(arr, c) - 1
            if r - l + 1 > (n/4):
                return c
        return -1
        