from sortedcontainers import SortedList
from collections import deque

class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.window = deque()
        self.sorted_window = SortedList()
        self.total_sum = 0

    def addElement(self, num: int) -> None:
        self.window.append(num)
        self.sorted_window.add(num)
        self.total_sum += num

        if len(self.window) > self.m:
            expired = self.window.popleft()
            self.sorted_window.remove(expired)
            self.total_sum -= expired

    def calculateMKAverage(self) -> int:
        if len(self.window) < self.m:
            return -1

        # Remove the smallest and largest k elements
        smallest_k_sum = sum(self.sorted_window[:self.k])
        largest_k_sum = sum(self.sorted_window[-self.k:])

        # Calculate the remaining sum
        mk_sum = self.total_sum - smallest_k_sum - largest_k_sum
        remaining_elements = self.m - 2 * self.k

        return mk_sum // remaining_elements
