class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tailIndex = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[tailIndex], nums[i] = nums[i], nums[tailIndex]
                tailIndex += 1


        