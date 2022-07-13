# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        # stores node.val : [(neighbords.val, u/l/r)]
        graph = collections.defaultdict(list)
        
        q = collections.deque([root])
        # BFS to create the directional graph
        while q:
            cur = q.popleft()
            
            if cur.left:
                # add neighbors and connection direciton to graph
                graph[cur.val].append((cur.left.val,'L'))
                graph[cur.left.val].append((cur.val,'U'))
                
                # append actual node to queue to continue tree BFS
                q.append(cur.left)
            if cur.right:
                graph[cur.val].append((cur.right.val,'R'))
                graph[cur.right.val].append((cur.val, 'U'))
                q.append(cur.right)
        
        #find shortest path from direction graph
        seen = set()
        # ndoes are (val, path)
        q.append((startValue, ''))
        while q:
            curVal, curPath = q.popleft()
            # found path
            if curVal == destValue:
                return curPath
            #avoid repeat checks
            seen.add(curVal)
            
            for neighbor,direction in graph[curVal]:
                if neighbor not in seen:
                    q.append((neighbor, curPath + direction))
                    
                    
                    
                    
            
            
            
            
            
        
        
        
