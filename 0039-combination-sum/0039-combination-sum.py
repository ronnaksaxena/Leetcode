class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        [2,3,5], target = 8
        output = [[2, 2, 2, 2], [2, 2, 3], [3,5]]
        
        combo = [2, 2, 3], curSum = 0
        terminal: if curSum == target: add copy to output
                  if curSum > target: return
        
        '''
        
        output = set()
        
        def backtrack(combo = [], curSum = 0):
            nonlocal output
            if curSum == target:
                output.add(copy.deepcopy(tuple(sorted(combo))))
                return
            if curSum > target:
                return
            for n in candidates:
                combo.append(n)
                backtrack(combo, curSum + n)
                combo.pop()
        
        backtrack()
        return list(output)
        