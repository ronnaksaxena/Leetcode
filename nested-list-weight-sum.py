#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
​
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        
        #BFS approach
        
        total = 0
        depth = 1
        
        q = collections.deque(nestedList)
        
        while q:
            for i in range(len(q)):
                nest = q.popleft()
                if nest.isInteger():
                    total += nest.getInteger() * depth
                else:
                    q.extend(nest.getList())
            depth += 1
            
        return total
        
        
        
        
        
        
        
        
