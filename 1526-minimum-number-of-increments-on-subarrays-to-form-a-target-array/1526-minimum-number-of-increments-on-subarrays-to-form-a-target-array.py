class Solution:
    def minNumberOperations(self, target: List[int]) -> int:

        prev, res = 0, 0

        for cur in target:
            if cur > prev:
                res += cur - prev

            prev = cur

        return res
        