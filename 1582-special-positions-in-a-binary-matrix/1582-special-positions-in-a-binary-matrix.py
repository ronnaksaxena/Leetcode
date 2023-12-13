class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        counts = product([sum(row) for row in mat], [sum(col) for col in zip(*mat)])
        return sum(rc == cc == val == 1 for (rc, cc), val in zip(counts, chain(*mat)))