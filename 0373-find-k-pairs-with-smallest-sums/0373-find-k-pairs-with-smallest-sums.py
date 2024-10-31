class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        N1, N2 = len(nums1), len(nums2)
        min_heap = [(nums1[0] + nums2[0], 0, 0)]
        res = []
        while min_heap and k:
            s, i1, i2 = heappop(min_heap)
            res.append((nums1[i1], nums2[i2]))
            k -= 1
            if i1 + 1 < N1: # add rows, like linkedlist items
                heappush(min_heap, (nums1[i1 + 1] + nums2[i2], i1 + 1, i2))
            if not i1 and i2 + 1 < N2: # add only first column
                heappush(min_heap, (nums1[i1] + nums2[i2 + 1], i1, i2 + 1))
        return res

        