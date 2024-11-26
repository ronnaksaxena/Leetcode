from sortedcontainers import SortedDict

class RangeModule:
    def __init__(self):
        self.d = SortedDict()
        
    def addRange(self, left: int, right: int) -> None:
        i = self.d.bisect_left(left)
        n = len(self.d)

        if i > 0 and list(self.d.values())[i - 1] >= left:
            i -= 1

        newStart, newEnd = left, right
        keysToRemove = []

        for j in range(i, n):
            curStart = list(self.d.keys())[j]
            curEnd = self.d[curStart]
            if curStart > newEnd:
                break
            keysToRemove.append(curStart)
            newStart = min(newStart, curStart)
            newEnd = max(newEnd, curEnd)

        for k in keysToRemove:
            del self.d[k]

        self.d[newStart] = newEnd

    def queryRange(self, left: int, right: int) -> bool:
        # Find the largest interval starting <= `left`
        i = self.d.bisect_right(left) - 1

        # If `i < 0`, there is no interval that could possibly cover `left`
        if i < 0:
            return False

        # Retrieve the range that might cover `left`
        rangeStart = list(self.d.keys())[i]
        rangeEnd = self.d[rangeStart]

        # Check if the entire `[left, right)` range is within the tracked interval
        return rangeStart <= left and rangeEnd >= right

    def removeRange(self, left: int, right: int) -> None:
        i = self.d.bisect_left(left)
        if i > 0 and list(self.d.values())[i - 1] > left:
            i -= 1

        keysToRemove = []
        intervalsToAdd = []
        n = len(self.d)

        for j in range(i, n):
            curStart = list(self.d.keys())[j]
            curEnd = self.d[curStart]
            if curStart >= right:
                break
            keysToRemove.append(curStart)
            if curStart < left:
                intervalsToAdd.append((curStart, left))
            if curEnd > right:
                intervalsToAdd.append((right, curEnd))

        for k in keysToRemove:
            del self.d[k]

        for s, e in intervalsToAdd:
            self.d[s] = e
