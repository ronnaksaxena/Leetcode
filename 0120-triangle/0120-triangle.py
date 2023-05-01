class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @lru_cache
        def dfs(i, level):
            if level == len(triangle):
                return 0
            
            left = triangle[level][i] + dfs(i, level + 1)
            right = triangle[level][i] + dfs(i+1, level + 1)
            
            return min(left, right)

        return dfs(0, 0)
            
            