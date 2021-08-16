class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B = nums1, nums2
        
        if len(B) < len(A):
            A, B, = B, A
        
        l, r = 0, len(A)-1
        while True:
            i = (r+l) // 2
            j = half - i - 2
            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i+1] if (i+1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if (j+1) < len(B) else float('inf')
            
            if Aleft <= Bright and Bleft <= Aright:
                
                if total%2 == 1:
                    return float(min(Aright, Bright))
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright)) / 2
                
            if Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
                
​
        
        return 1.0
