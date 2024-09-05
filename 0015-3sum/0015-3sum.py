class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def helper(start, output, nums):
            lo, hi = start+1, len(nums)-1
            while lo < hi:
                val = nums[start] + nums[lo] + nums[hi]
                # too small
                if val < 0:
                    lo += 1
                # too big
                elif val > 0:
                    hi -= 1
                # add to tuple
                else:
                    output.append([nums[start], nums[lo], nums[hi]])
                    lo += 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    hi -= 1
            return
        nums.sort()
        output = []

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                helper(i, output, nums)

        return output

        