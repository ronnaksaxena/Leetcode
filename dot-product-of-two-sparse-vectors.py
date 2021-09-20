class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
    
    def getNums(self):
        return self.nums
​
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        other = vec.getNums()
        res = 0
        for x,y in zip(self.nums, other):
            res += x*y
        return res
        
​
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
