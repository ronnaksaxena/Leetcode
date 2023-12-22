class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        n = 4, k = 2
        [1,2,3,4]
    /                   |.      |.     \
[1]                     [2]     [3].  [4]
|  \ \  
[1,2] [1,3] [1,4]      [2, 3] [2,4]

have start i and loop j for all other picks
if len array you're building == k add to output
if i > options to pick discard question
        '''
        
        output = []
        
        def backtrack(cur, i):
            nonlocal output
            if i > n+1:
                return
            if len(cur) == k:
                output.append(cur[::])
                return
            for j in range(i, n+1):
                cur.append(j)
                backtrack(cur, j+1)
                cur.pop()
        backtrack([], 1)
        return output