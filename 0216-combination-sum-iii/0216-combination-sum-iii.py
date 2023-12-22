class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        output = []
        
        def backtrack(cur, i, sumLeft):
            nonlocal output
            if sumLeft < 0 or i > 10 or len(cur) > k:
                return
            if sumLeft == 0 and len(cur) == k:
                output.append(cur[::])
                return
            for num in range(i, 10):
                cur.append(num)
                backtrack(cur, num+1, sumLeft - num)
                cur.pop()
        
        backtrack([], 1, n)
        return output
        