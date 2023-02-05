class NumArray:

    def __init__(self, nums: List[int]):
        '''
        nums =    [-2, 0, 3, -5, 2, -1]
        prefixSum [-2, -2, 1, -4, -2, -3]
        
        sum(nums[a->b]) = prefixSum[b]-(prefixSum[a-1] if a > 0 else 0)
        
        '''
        self.pre = [0 for _ in range(len(nums))]
        running = 0
        for i, n in enumerate(nums):
            running += n
            self.pre[i] = running
            
        

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right] - (self.pre[left-1] if left > 0 else 0)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)