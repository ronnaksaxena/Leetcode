class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        # The minumum length of the ribbon that we can cut is 1
        start = 1
        # The maximum length of the ribbon can be the maximum element in the list
        end = max(ribbons)
        
        # In this binary search, we are trying to go through the origin list and figure out which integer(from 1 -> ribbon of max length) is the deired length for the the target k pieces
        while(start <= end):
            mid = start + (end - start) // 2
            res = 0
            for i in ribbons:
                res += i // mid
            # If the value is >= target, we know that there could be a larger integer that will satisfy the same conditon
            if res >= k:
                start = mid+1
            else:
            # If lesser than k, then there could be a value lesser than the mid that could satisfy the condition
                end = mid -1
        return end
        