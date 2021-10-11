class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        totalNums = list(set(nums1)) + list(set(nums2)) + list(set(nums3))
        map = collections.Counter(totalNums)
        
        return [i for i,v in map.items() if v >=2]
        
