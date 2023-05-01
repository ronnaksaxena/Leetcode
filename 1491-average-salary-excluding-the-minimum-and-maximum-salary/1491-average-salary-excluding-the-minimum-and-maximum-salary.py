class Solution:
    def average(self, salary: List[int]) -> float:
        minSal, maxSal, total = min(salary), max(salary), sum(salary)
        
        total -= (minSal + maxSal)
        return total / (len(salary) - 2)
        
        