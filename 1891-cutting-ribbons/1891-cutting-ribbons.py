class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        '''
        - can either cut ribbon or not cut, can through away excess ribbon
        - return 0 if not possible to make k ribbons
        
        if ribbon is size x and we cut each piece into size y
            # of equal lenght ribbons is x // y
        
        smallest possible lenghth is 1
        largest possible length is max(ribbons)
        
        Ideas: Binary search between1 and max(ribbons) to find largest cut size
        - helper function (cutSize) returns the number of ribbons yeielded
        - Bsearch betwen 1 -> max(ribbosn):
            cutSize = median of bounds
            if helper(cutSize) >= k:
                l = cutSize
            else:
                r = cutSize - 1 # cutSize too big, not enough pieces
        
        check if 1 works otherwise 0
        
        Time: O(log(max ribbon))
        Space: O(1)
        '''
        
        def ribbonPieces(cutSize):
            return sum(r // cutSize for r in ribbons)
        
        l, r = 1, max(ribbons)
        while l <= r:
            cutSize = l + (r-l)//2
            if ribbonPieces(cutSize) >= k:
                l = cutSize + 1
            else:
                r = cutSize - 1
        return r
        