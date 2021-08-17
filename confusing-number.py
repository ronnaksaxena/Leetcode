class Solution:
    def confusingNumber(self, n: int) -> bool:
        valids = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        digits = [d for d in str(n)]
        invalids = {'2','3','4','5','7'}
        
        newNum = []
        
        for d in digits:
            if d in invalids:
                return False
            
            newNum.append(valids[d])
            
​
            
        return int(''.join(newNum[::-1])) != n
