class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(1, n+1)]
        lastPlayer = 0
        while len(players) > 1:
            removedPlayer = lastPlayer
            for _ in range(k-1):
                removedPlayer = (removedPlayer + 1) % len(players)
            # set to next player before removing from list
            players.remove(players[removedPlayer])
            lastPlayer = removedPlayer%len(players)
        return players[0]
                
            
        