class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        alt = 0
        for a in gain:
            alt += a
            ans = max(ans, alt)
        return ans
        