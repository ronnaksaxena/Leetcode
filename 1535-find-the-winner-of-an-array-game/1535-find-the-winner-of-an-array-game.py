class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner, winCount = -1, 0
        q = collections.deque(arr)
        if k > len(arr):
            k = len(arr)%k
        while winCount < k:
            # Find winner
            # print(q, winner, winCount)
            val1, val2 = q.popleft(), q.popleft()
            curWinner = max(val1, val2)
            curLoser = val1 if curWinner == val2 else val2
            if curWinner == winner:
                winCount += 1
            else:
                winner = curWinner
                winCount = 1
            # rotate q
            q.appendleft(curWinner)
            q.append(curLoser)
        return winner
        