class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        increasing = True
        
        for i in range(1,len(arr)):
            if arr[i] == arr[i-1]:
                return False
            if i == 1:
                if arr[i] <= arr[i-1]:
                    return False
            elif increasing:
                    if arr[i] < arr[i-1]:
                        increasing = False
            else:
                    if arr[i] >= arr[i-1]:
                        return False
        return not increasing
