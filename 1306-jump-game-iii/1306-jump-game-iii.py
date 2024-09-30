class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        def getNextJumps(index):
            # Returns [indices can jump to]
            ans = []
            pre = index - arr[index]
            if 0 <= pre < n:
                ans.append(pre)
            post = index + arr[index]
            if 0 <= post < n:
                ans.append(post)
            return ans

        q = collections.deque([start])
        visited = {start}

        while q:
            cur = q.popleft()
            if arr[cur] == 0:
                return True
            for jump in getNextJumps(cur):
                if jump not in visited:
                    visited.add(jump)
                    q.append(jump)
        return False
        