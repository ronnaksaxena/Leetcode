class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        '''
        [1,1,2,2,3,3,4,4,5,5], target = 8
         i
               j
                           k
        
        
        '''
        
        arr.sort()
        count = 0
        
        for i,x in enumerate(arr):
            T = target-arr[i]
            j, k = i+1, len(arr)-1
            
            while j<k:
                if arr[j]+arr[k] > T:
                    k -= 1
                elif arr[j]+arr[k] <T:
                    j += 1
                elif arr[j] != arr[k]: # We have A[j] + A[k] == T.
                    # Let's count "left": the number of A[j] == A[j+1] == A[j+2] == ...
                    # And similarly for "right".
                    left = right = 1
                    while j + 1 < k and arr[j] == arr[j+1]:
                        left += 1
                        j += 1
                    while k - 1 > j and arr[k] == arr[k-1]:
                        right += 1
                        k -= 1
​
                    # We contributed left * right many pairs.
                    count += left * right
                    j += 1
                    k -= 1
                else: #arr[j] == arr[k]
                    count += (k-j+1) * (k-j) // 2
                    break
                    
        return count%(10**9+7)
