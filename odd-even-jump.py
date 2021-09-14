class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        next_higher, next_lower = [0 for _ in range(n)], [0 for _ in range(n)]
        stack = []
        for a, i in sorted([a,i] for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)
            
        stack = []
        for a, i in sorted([-a,i] for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)
            
        higher, lower = [False for _ in range(n)], [False for _ in range(n)]
        higher[-1], lower[-1] = True, True
        
        for i in range(n-2,-1,-1):
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
            
