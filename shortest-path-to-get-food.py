class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, -1), (0, 1), (1, 0), (-1,0)]
        seen = set()
        
        #1 .find the person
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '*':
                    start = (r,c)
                    break
        
        deque = collections.deque([start])
        res = 0
​
        
        while deque:
            size = len(deque)
            
            # we only need finish the search at current level 
            # then go to next level
            for _ in range(size):
                currR, currC = deque.popleft()
