class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0

        # Calculate the winner using mathematical formula
        for i in range(2, n + 1):
            winner = (winner + k) % i

        # Adjust for 0-based indexing
        return winner + 1
        