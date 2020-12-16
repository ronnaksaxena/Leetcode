class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        g1 = [(k,len(list(grp))) for k,grp in itertools.groupby(name)]
        g2 = [(k,len(list(grp))) for k,grp in itertools.groupby(typed)]
        
        if len(g1) != len(g2):
            return False
        
        for (k1,v1),(k2,v2) in zip(g1,g2):
            if k1!=k2:
                return False
            if v1 > v2:
                return False
        return True
