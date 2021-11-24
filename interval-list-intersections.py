class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        output = []
        
        i = j = 0
        
        A = firstList
        B = secondList
        
        while i < len(A) and j < len(B):
            
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                output.append([lo, hi])
            
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
                
                
        return output
