class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        maxNum, minNum = float('-inf'), float('inf')
        for i in '0123456789':
            for j in '0123456789':
                nextNum = num.replace(i, j)
                if nextNum[0] == '0' or int(nextNum) == 0:
                    continue
                maxNum = max(maxNum, int(nextNum))    
                minNum = min(minNum, int(nextNum))    
        return maxNum - minNum 
        