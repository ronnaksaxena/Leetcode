class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        q = collections.deque([(0,0)])
        visited = set()
        while q:
            curR, curC = q.popleft()
            ans.append(nums[curR][curC])
            
            if curR + 1 < len(nums) and curC < len(nums[curR+1]) and (curR+1,curC) not in visited:
                q.append((curR+1, curC))
                visited.add((curR+1, curC))
            if curC + 1 < len(nums[curR]) and (curR, curC+1) not in visited:
                q.append((curR, curC+1))
                visited.add((curR, curC+1))
        return ans
        