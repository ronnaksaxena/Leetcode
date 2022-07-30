class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # Sorting to skip duplicate numbers adjacent to each other
        nums.sort()
        
        def backtrack(i, subset, output):
            if i == n:
                output.append(subset[:])
                return
            
            # Create all combos including elem i
            subset.append(nums[i])
            backtrack(i+1, subset, output)
            
            # Avoid duplicate elems in subset
            while (i+1) < n and nums[i] == nums[i+1]:
                i += 1
            
            # Create all combos excluding elem i
            subset.pop()
            backtrack(i+1, subset, output)
            
        output = []
        backtrack(0, [], output)
        return output
        
