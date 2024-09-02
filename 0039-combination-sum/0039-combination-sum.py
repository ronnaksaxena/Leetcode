class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
    candidates = [2,3,6,7], target = 7

i              [2, 2, 3]

Backtrack:
    Terminals
    - if sum == target: add to output
    - if sum > target: return

    - pick element
    - dont pick element
        '''

        output = []
        
        def backtrack(i=0, combo=[], curSum = 0):
            nonlocal output
            if curSum == target:
                output.append(combo[:])
                return
            if curSum > target:
                return
            if i == len(candidates):
                return
            # Pick
            combo.append(candidates[i])
            backtrack(i, combo, curSum + candidates[i])
            # Don't pick
            combo.pop()
            backtrack(i+1, combo, curSum)

        backtrack()
        return output

        


        