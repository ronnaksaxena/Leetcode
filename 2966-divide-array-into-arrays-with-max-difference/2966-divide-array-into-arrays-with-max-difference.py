class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        '''
        input: list[int], k: int
        output: List[List[3]]
        
        Positive int, k
        Length of nums div by 3
        
        [1,3,4,8,7,9,3,5,1]
        
        [[1,1,_], [1,_,_], [3,_,_]]
          
        [1,1,3,3,4,5,7,8,9]
           i
           
        Algo:
            - iterate thorught sorted list
            - append element to respective bucket, if any elemnt in bucket had difference > k
                - return []
        Time: O(nlogn) to sort the input list
        Space: O(1)
        '''
        buckets = len(nums) // 3
        output = [[0,0,0] for _ in range(buckets)]
        curBucket = 0
        curIndex = 0
        nums.sort()
        for n in nums:
            output[curBucket][curIndex] = n
            # print(output, n)
            # Check if valid bucket
            if curIndex == 1 and output[curBucket][1] - output[curBucket][0] > k:
                return []
            if curIndex == 2 and (output[curBucket][2] - output[curBucket][1] > k) or (output[curBucket][2] - output[curBucket][0] > k):
                return []
            
            # Move ptrs
            if curIndex < 2:
                curIndex += 1
            else:
                curIndex = 0
                curBucket += 1
        return output
        
        