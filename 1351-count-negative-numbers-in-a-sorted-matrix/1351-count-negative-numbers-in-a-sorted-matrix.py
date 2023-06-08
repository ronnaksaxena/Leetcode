class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def bSearch(arr):
            l, r = 0, len(arr)
            while l < r:
                m = l + (r-l)//2
                if arr[m] >= 0:
                    l = m + 1
                else:
                    r = m
            return l
        
        count = 0
        rowLength = len(grid[0])
        for row in grid:
            # sorted in decreased order so all neg elements will be left of first neg
            '''
            0 0 0 -1
            0 1 2 3
            '''
            count += (rowLength - bSearch(row)) 
        
        return count
        