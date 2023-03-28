class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        output = []

        for i in range(len(nums)-2):
            # ignore duplicates
            # skip the one before becuase you don't want to miss a set that could contain a duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # too big numbers
            if nums[i] > 0:
                break
            l, r = i + 1, len(nums)-1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val < 0:
                    l += 1
                elif val > 0:
                    r -= 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    #avoid more left duplicates
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return output
