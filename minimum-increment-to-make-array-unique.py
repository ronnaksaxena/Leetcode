class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        dups = []
        count = 0
        
        for n in range(len(nums)+max(nums)):
            if freq[n] > 1:
                dups.extend([n] * (freq[n]-1))
            elif dups and not freq[n]:
                last = dups.pop()
                count += n - last
        
        return count
        
        
