# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        l = 0
        r = 1
        
        while reader.get(r) < target:
            l = r
            r *= 2
        
        while l <= r:
            m = l + (r-l)//2
            val = reader.get(m)
            if val == target:
                return m
            elif l == r:
                break
            elif val < target:
                l = m + 1
            else:
                r = m
        
        return -1
        