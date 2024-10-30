class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        - combinations include [1,n] of size k

        n = 4, k = 2
        1, 2, 3, 4
        [].  -> loop throught remaining potential candidates
    /.   /.   \.  - i+1 -> (n-k)
    [1].    [2]  [3]
  /. \. \.      / \.  |
[1,2] [1,3] [1,4] [2,3] [2,4] [3,4] => terminate if size of combnation == k

Time: O(n^k)
Space: O(k)
        '''

        output = []

        def backtrack(cur=[], leftBound=1):
            nonlocal output
            if len(cur) == k:
                output.append(cur[:])
                return
            start = cur[-1]+1 if cur else 1
            for candidate in range(start, n+1):
                cur.append(candidate)
                backtrack(cur)
                cur.pop()

        backtrack()
        return output
        