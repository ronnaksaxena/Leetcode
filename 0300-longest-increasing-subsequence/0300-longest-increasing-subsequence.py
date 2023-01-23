class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        sub = []
        for n in nums:
            index = bisect.bisect_left(sub, n)
            # Largest value in subsequence
            if index == len(sub):
                sub.append(n)
            else:
                sub[index] = n
        return len(sub)
        