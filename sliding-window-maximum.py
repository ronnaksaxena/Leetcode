class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        
        l, r = 1, k
        q = collections.deque()
        output = []
        for i in range(k):
            if not q:
                q.append(i)
            elif nums[i] <= nums[q[-1]]:
                q.append(i)
            else:
                while q and nums[i] > nums[q[-1]]:
                    q.pop()
                q.append(i)
        output.append(nums[q[0]])
        
        while r < len(nums):
            
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            
            if q and l > q[0]:
                q.popleft()
            
            q.append(r)
            
            r += 1
