class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        small = nums1 if len(nums1) < len(nums2) else nums2
        big = nums2 if len(nums2) > len(nums1) else nums1
        s = set(small)
        b = set(big)
        ans = []
        for n in s:
            if n in b:
                ans.append(n)
        return ans
        
        