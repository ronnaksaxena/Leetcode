# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:
​
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dims = binaryMatrix.dimensions()
        rows, cols = dims[0], dims[1]
        res = -1
        r, c = rows-1, cols-1
        
        while r >= 0 and c >= 0:
            
            if binaryMatrix.get(r,c):
                res = c
                c -= 1
            else:
                r -= 1
                
        return res
        
