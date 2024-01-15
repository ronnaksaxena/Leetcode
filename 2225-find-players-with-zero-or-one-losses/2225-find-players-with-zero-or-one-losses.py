class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        '''
        - playerid unique
        - values returns in increasing order
        
        idea: hashmap
            {player: [wins, losses]}
        
        loop throught key values pairs in map:
            - add to output[0] if no losses
            - add to output[1] if 1 one loss
        - sort output
        -return desired values
        
        Time: O(nlogn)
        Space: O(n)
        '''
        
        playerWins = {} # {playerId: [wins, losses]}
        for winner, loser in matches:
            if winner not in playerWins:
                playerWins[winner] = [0,0]
            if loser not in playerWins:
                playerWins[loser] = [0,0]
            
            # increment record
            playerWins[winner][0] += 1
            playerWins[loser][1] += 1
        
        output = [[], []]
        for player, (wins, losses) in playerWins.items():
            if losses == 0:
                output[0].append(player)
            elif losses == 1:
                output[1].append(player)
        output[0].sort()
        output[1].sort()
        return output