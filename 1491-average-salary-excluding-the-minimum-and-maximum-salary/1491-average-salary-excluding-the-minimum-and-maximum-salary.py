class Solution:
    def average(self, salary: List[int]) -> float:
        minSal, maxSal, total = float('inf'), float('-inf'), 0
        for s in salary:
            total += s
            minSal = min(minSal, s)
            maxSal = max(maxSal, s)
        
        total -= (minSal + maxSal)
        return total / (len(salary) - 2)
        
        