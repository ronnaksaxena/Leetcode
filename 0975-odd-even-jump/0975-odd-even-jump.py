class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1  # Single element array always has 1 good index

        # Precompute next valid indices for odd and even jumps
        def makeNext(isOddJump):
            sorted_indices = sorted(range(n), key=lambda i: (arr[i], i) if isOddJump else (-arr[i], i))
            stack = []
            next_jump = [None] * n
            for i in sorted_indices:
                while stack and stack[-1] < i:
                    next_jump[stack.pop()] = i
                stack.append(i)
            return next_jump

        next_odd = makeNext(True)
        next_even = makeNext(False)

        # Dynamic Programming arrays
        odd = [False] * n
        even = [False] * n
        odd[-1] = even[-1] = True  # Base case: last index always reaches itself

        for i in range(n - 2, -1, -1):
            if next_odd[i] is not None:
                odd[i] = even[next_odd[i]]
            if next_even[i] is not None:
                even[i] = odd[next_even[i]]

        # Count all indices that are "good" starting points
        return sum(odd)
