class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        '''
        k = 3, n = 7
        
        []
|   |   |   |   |   |   |
[1] [2] [3] [4] [5] [6] [7]
/\

        
        '''
        global output
        output = []
        def backtrack(cur=[], i=1, remain=n):
            if len(cur) == k and remain == 0:
                # Found valid combo
                output.append(cur[::])
                return
            if len(cur) > k or remain < 0:
                # Can't add any more
                return
            # All remaining numbers
            for j in range(i, 10):
                cur.append(j)
                backtrack(cur, j+1, remain - j)
                cur.pop()
                
        backtrack()
        return output
        