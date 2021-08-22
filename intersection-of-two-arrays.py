class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        small, big = nums1, nums2
        if len(nums1) > len(nums2):
            small, big = nums2, nums1
            
        sPtr, bPtr = 0,0
        output = []
        
        while sPtr < len(small) and bPtr < len(big):
            
            curSmall, curBig = small[sPtr], big[bPtr]
            
            if curSmall == curBig:
                output.append(curSmall)
                
                while sPtr < len(small) and small[sPtr] == curSmall:
                    sPtr += 1
                    
                while bPtr < len(big) and big[bPtr] == curBig:
                    bPtr += 1
                    
                continue
                
            if curSmall < curBig:
                while sPtr < len(small) and small[sPtr] == curSmall:
                    sPtr += 1
            else:
