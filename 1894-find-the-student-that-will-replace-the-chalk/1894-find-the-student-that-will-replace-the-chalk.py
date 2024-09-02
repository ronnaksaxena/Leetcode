class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for student, c in enumerate(chalk):
            k -= c
            if k < 0:
                return student
        
        return len(chalk) - 1
        