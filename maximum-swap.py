class Solution:
    def maximumSwap(self, num: int) -> int:
        
        if 0 <= num <= 10:
            return num
        
        num = str(num)
        idx = [0 for _ in range(len(num))]
        val = [0 for _ in range(len(num))]
        
        idx[-1], val[-1] = len(num)-1, num[-1]
        
        for i in range(len(num)-2,-1,-1):
            if num[i] > val[i+1]:
                val[i] = num[i]
                idx[i] = i
            else:
                val[i] = val[i+1]
                idx[i] = idx[i+1]
                
        swapIdx = -1
        
        for i in range(len(num)):
            if num[i] < val[i]:
                swapIdx = i
                break
        if swapIdx == -1:
            return int(num)
        
        res = num[:swapIdx] + num[idx[swapIdx]] + num[swapIdx+1:idx[swapIdx]] +num[swapIdx] + num[idx[swapIdx]+1:]
        return int(res)
            
