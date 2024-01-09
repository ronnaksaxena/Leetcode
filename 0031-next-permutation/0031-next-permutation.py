class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        
        1. iterate backwards find first decreasing element (pivot)
        2. find element to right of pivot that is next greatest value
            -if duplicate values pick right most
        3. swap pivot with next greatest integer
        4. reverse values to right of pivot
        
        1. 
        [1,5,8,4,7,6,5,3,1]
               ^
               |
               p
        2.
        [1,5,8,4,7,6,5,3,1]
                     ^
                     |
                     next Greatest int
        3.
        swap
        [1,5,8,5,7,6,4,3,1]
                 ^       ^
                 |       |
                reverse this area
        4. 
        [1,5,8,5,1,3,4,6,7]
        
        '''
        pivot = -1
        # Find first non increasing number from left
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        # Largest possible number, return smallest perm
        if pivot == -1:
            l = 0
            r = len(nums) -1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return nums
        # print('pivot', nums[pivot])
        # Next largest value
        swapVal, swap = inf, pivot
        for i in range(pivot+1, len(nums)):
            # If there are duplicate values pick right most
            if nums[i] > nums[pivot] and nums[i] <= swapVal:
                swap = i
                swapVal = nums[i
                              ]
        # No solution => Will never happen if pivot is found
        if swap == pivot:
            return nums
        # print('swap with', swap, nums[swap])
        # Swap these two
        nums[pivot], nums[swap] = nums[swap], nums[pivot]
        # print(nums)
        
        # Reverse remainig chars
        l = pivot+1
        r = len(nums) -1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        # print('reverse', nums)

        return nums
        