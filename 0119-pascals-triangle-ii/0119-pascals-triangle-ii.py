class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        pre = self.getRow(rowIndex-1)
        output = [1 for _ in range(rowIndex+1)]
        
        for i in range(1, len(pre)):
            output[i] = pre[i-1] + pre[i]
        
        return output
                
        