class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        return self.help(nums1[:], nums2[:])
    
    def help(self,nums1,nums2):
        if not nums1 or not nums2:
            return []
        if nums1[0]==nums2[0]:
            return [nums1[0]] + self.help(nums1[1:],nums2[1:])
        if nums1[0]>nums2[0]:
            return self.help(nums1,nums2[1:])
        else:
            return self.help(nums1[1:],nums2)
