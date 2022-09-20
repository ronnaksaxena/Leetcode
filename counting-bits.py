class Solution:
    def countBits(self, n: int) -> List[int]:
        
        output = []
        
        for i in range(n+1):
            ones = 0
            j = i
            while j:
                ones += j & 1
                j >>= 1
            output.append(ones)
            
        return output
        
