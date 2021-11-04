class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        
        ans = [0]
        queue = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
        while queue: 
            x = queue.popleft()
            if x <= high: 
                ans.append(x)
                for dd in x%10-1, x%10+1: 
                    if 0 <= dd < 10: queue.append(10*x+dd)
        return [x for x in ans if low <= x]
                    
                
        
