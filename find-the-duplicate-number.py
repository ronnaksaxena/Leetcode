class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        if nums[0] == nums[nums[0]]:
            return nums[0]
        else:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
            return self.findDuplicate(nums)
        
