class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Iterate through remaining indices and switch elements
        Branching factor decreases
        [1,2,3]
        / \. \
      [1,2,3] [2, 1, 3] [3, 2, 1]
      / \.      /\.       /\
      [1,2, 3] [1, 3, 2]

      - Can trim final level by terminating at index == n -1

      time : O(n + n -1 + n -2 + n-3)
      Space: O(n) for stack
        '''

        output = []
        n = len(nums)
        def backtrack(start=0):
            nonlocal nums, output
            if start == len(nums) -1:
                output.append(nums[:])
                return
            for end in range(start, len(nums)):
                # swap
                nums[start], nums[end] = nums[end], nums[start]
                backtrack(start+1)
                # swap back
                nums[start], nums[end] = nums[end], nums[start]

        backtrack()

        return output