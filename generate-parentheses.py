class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==1:
            return ['()']
        res = []
        
        def backtrack(openPar, closePar, cur, res):
            if openPar==0 and closePar==0:
                res.append(cur)
                return
            if 0 < openPar <= closePar:
                backtrack(openPar-1,closePar, cur + '(', res)
            if closePar >= openPar:
                backtrack(openPar, closePar-1, cur + ')', res)
        
        
        backtrack(n,n,'',res)
        
        return res
        
