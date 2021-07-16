class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        l, r = 0, len(arr)-1
        
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            if arr[mid-1] < arr[mid]:
                l = mid+1
            else:
                r = mid-1
        
        return l
    
​
