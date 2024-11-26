from sortedcontainers import SortedDict

class RangeModule:
    def __init__(self):
        self.intervals = SortedDict()

    def addRange(self, left: int, right: int) -> None:
        # Find the position to start merging
        start = self.intervals.bisect_left(left)
        if start > 0 and self.intervals.values()[start - 1] >= left:
            start -= 1

        # Merge overlapping intervals
        new_start, new_end = left, right
        keys_to_remove = []
        for i in range(start, len(self.intervals)):
            curr_start = self.intervals.keys()[i]
            curr_end = self.intervals[curr_start]
            if curr_start > right:
                break
            new_start = min(new_start, curr_start)
            new_end = max(new_end, curr_end)
            keys_to_remove.append(curr_start)

        for key in keys_to_remove:
            self.intervals.pop(key)
        self.intervals[new_start] = new_end

    def removeRange(self, left: int, right: int) -> None:
        # Find the position to start splitting
        start = self.intervals.bisect_left(left)
        if start > 0 and self.intervals.values()[start - 1] > left:
            start -= 1

        # Split overlapping intervals
        keys_to_remove = []
        new_intervals = []
        for i in range(start, len(self.intervals)):
            curr_start = self.intervals.keys()[i]
            curr_end = self.intervals[curr_start]
            if curr_start >= right:
                break
            keys_to_remove.append(curr_start)
            if curr_start < left:
                new_intervals.append((curr_start, left))
            if curr_end > right:
                new_intervals.append((right, curr_end))

        for key in keys_to_remove:
            self.intervals.pop(key)
        for start, end in new_intervals:
            self.intervals[start] = end

    def queryRange(self, left: int, right: int) -> bool:
        # Find the interval that might contain [left, right)
        start = self.intervals.bisect_right(left) - 1
        if start < 0:
            return False
        return self.intervals.values()[start] >= right

