class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        mps = 0
        for i in range(len(nums)):
            mps = max(mps, nums[i] + nums[len(nums)-1-i])
        return mps