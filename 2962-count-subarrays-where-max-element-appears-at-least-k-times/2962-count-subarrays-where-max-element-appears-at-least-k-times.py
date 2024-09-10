class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        '''
        input; Arr[int], k:int
        output: int

        -empty arr? => no
        - multiple maxes? => possible
        - int overflow? neg? => 1 <= nums[i] <= 10^6

[1,3,2,3,3], k = 2
         e
          s

IW = 2
        '''

        maxNum = max(nums)
        ans = start = 0
        inWindow = 0
        for end in range(len(nums)):
            if nums[end] == maxNum:
                inWindow += 1
            while inWindow == k:
                if nums[start] == maxNum:
                    inWindow -= 1
                start += 1
            ans += start

        return ans

        