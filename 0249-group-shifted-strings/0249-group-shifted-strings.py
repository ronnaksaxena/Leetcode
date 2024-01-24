class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        '''
        -lowercase letters
        - non null
        
        'a' cant be shifted to any char
        "abc" "bcd" "xyz"
          1 1   1 1.  1 1
          
          Edge case we need to mod our shifts by 26 to handle z
          -1%26 => 25
          (ASCII(a) - ASCII(b)) % 26 => 25
          
         Idea: Hash table {steps away from each char: [strings]}
         
        ["abc","bcd","acef","xyz","az","ba","a","z"]
        
        {
            (1,1): ['abc', 'bcd', 'xyz']
            (25):
            
        }
        
        - helper function to generate hash tuple
        - loop thought all strings and store groups by hash in our hash table
        
        '''
        def generateHash(s):
            order = []
            for i in range(1, len(s)):
                second = ord(s[i]) - ord('a')
                first = ord(s[i-1]) - ord('a')
                order.append((second-first)%26)
            return tuple(order)
                             
        
        groups = collections.defaultdict(list)
        for s in strings:
            groups[generateHash(s)].append(s)

        return groups.values()
        