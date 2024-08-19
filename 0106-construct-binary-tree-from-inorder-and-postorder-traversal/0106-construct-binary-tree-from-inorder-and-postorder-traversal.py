# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        '''
        input: 2 lists
        output: Treenode
        
        Edge cases
        - valid input
        - empty arr returns null
        - no duplicate values
        
        inorder = [9,3,15,20,7]
                   0,1,2, 3, 4
                             i
                    
        postorder = [9,,]
                    ^
                    |
                    root
                                
                                
            3
        /       \
        9       20
             /.     \
             15.     7
                          
        Process:
        pop root from end of the postorder
        rec build the right subtree root.right = dfs(index+1, right)
        rec build the left subtree root.left = dfs(left, index-1)
        
        PSUEDOCODE:
        
        map = {val: index in inOrderTraversal}
        dfs helper (left, right)
            1. if left > right or postOrder is null"
                return null
            2. root => pop from end of post order
            3. initalize root node
            3. build right subtree root.right = dfs(index+1, right)
            4. Build left subtree root.left = dfs(left, index-1)
        
        return dfs(0, n -1)
        
        
        time: O(n) where n is elements in lists
        space: O(n) to precompute the list
            
            
        '''
        
        iot = {val: index for index, val in enumerate(inorder)}
        
        def dfs(left, right):
            if left > right:
                return None
            rootVal = postorder.pop()
            root = TreeNode(rootVal)
            index = iot[rootVal]
            root.right = dfs(index+1, right)
            root.left = dfs(left, index-1)
            return root
        
        return dfs(0, len(inorder)-1)
        