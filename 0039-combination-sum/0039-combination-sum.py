class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        [2,3,5], target = 8
        output = [[2, 2, 2, 2], [2, 2, 3], [3,5]]
        
        combo = [2, 2, 3], curSum = 0
        terminal: if curSum == target: add copy to output
                  if curSum > target: return
        
        '''
        
        output = []
        
        def backtrack(combo = [], curSum = 0, start = 0):
            nonlocal output
            if curSum == target:
                output.append(copy.deepcopy(combo))
                return
            if curSum > target:
                return
            for i in range(start, len(candidates)):
                combo.append(candidates[i])
                backtrack(combo, curSum + candidates[i], i)
                combo.pop()
        
        backtrack()
        return list(output)
        