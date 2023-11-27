class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        preSum -> sum(A[i] -> A[j]) == A[j] - (A[i-1] if i > 0 else 0)
        Algo:
        1. init preSum
        2. loop  j thought nums:
            if sum(A[:j]) == sum(A[j+1:]):
            return j
        3. otherwise ret -1
        '''
        if len(nums) == 1:
            return 0
        pre = [nums[0]]
        for n in nums[1:]:
            pre.append(pre[-1] + n)
        
        for j in range(len(nums)):
            if (pre[j-1] if j > 0 else 0) == pre[-1] - pre[j]:
                return j

        return -1
        