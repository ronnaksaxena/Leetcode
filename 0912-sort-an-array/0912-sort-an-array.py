class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            return merge(left, right)
    
        def merge(left, right):
            output = []
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    output.append(left[l])
                    l += 1
                else:
                    output.append(right[r])
                    r += 1
            output.extend(left[l:])
            output.extend(right[r:])
            return output
    
        return mergeSort(nums)
                    
        