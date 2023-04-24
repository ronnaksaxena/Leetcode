class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        q = collections.deque()
        window = set()
        for n in nums:
            if n in window:
                return True
            q.append(n)
            window.add(n)
            while len(q) > k:
                window.remove(q.popleft())
        
        return False
            
        