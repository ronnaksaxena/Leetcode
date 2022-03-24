class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if not people:
            return 0
        count = 0
        i, j = 0, len(people)-1
        people.sort()
        
        while i <= j:
            count += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            
        return count
        
        
        '''
        l = 3
        1, 2, 2, 3
        
        cur = 1
        count = 1
        
        if p[i] + cur > l:
            cur = p[i]
            count ++
