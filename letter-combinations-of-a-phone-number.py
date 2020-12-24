class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        
        mapping = [
            '0',
            '1',
            'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz'
        ]
        
        self.helper(res,digits,'',0,mapping)
        return res
    
    def helper(self,res,digits,cur,idx,mapping):
        if len(cur)==len(digits):
            res.append(cur)
            return
        else:
            combos = mapping[int(digits[idx])]
            for letter in combos:
                self.helper(res,digits,cur+letter,idx+1,mapping)
            
            
            
            
            
            
            
