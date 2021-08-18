class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        n = len(num)
        output = []
        
        def backtrack(idx, pre, cur, val, s):
            if idx == n:
                if val == target and cur == 0:
                    output.append(s)
                return
            
            cur = cur * 10 + int(num[idx])
            
            if cur > 0:
                backtrack(idx+1, pre, cur, val, s)
                
            if not s:
                backtrack(idx+1, cur, 0, cur, str(cur))
                
            else:
                backtrack(idx+1, cur, 0, val+cur, s + '+' + str(cur))
                backtrack(idx+1, -cur, 0, val-cur, s + '-' + str(cur))
                backtrack(idx+1, pre * cur, 0, val-pre+pre*cur, s + '*' + str(cur))
                
