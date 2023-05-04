class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        remR, remD = 0, 0
        numSenators = collections.Counter(senate)
        q = collections.deque()
        for s in senate:
            q.append(s)
        
        while q:
            # print(q, remR, remD)
            # print(numSenators)
            s = q.popleft()
            if s == 'R' and remR > 0:
                numSenators[s] -= 1
                remR -= 1
                continue
            elif s == 'D' and remD > 0:
                numSenators[s] -= 1
                remD -= 1
                continue
            nextSen = 'R' if s == 'D' else 'D'
            if nextSen == 'R':
                remR += 1
            else:
                remD += 1
            q.append(s)
            if numSenators[nextSen] == 0:
                break
        return 'Radiant' if q[0] == 'R' else 'Dire'
            
        