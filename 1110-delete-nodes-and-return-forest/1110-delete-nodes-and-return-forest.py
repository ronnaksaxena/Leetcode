# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        '''
        input? rootNode
        output: list[rootNode]

        Clarify:
        - Are there duplicate values in the root tree?
        - Memory constrains is there int overflow or # of nodes too big?
        - Order of list does not matter


        Idea: Bottom up Post Order approach:

        global return list
        post order traversal of root
        if current node to process is to delete add children to forest list if they are not null

                        1
                        /\
                        2 
                    /\.    /\
                    4 .   6 7


                    forest [[6], [7], [1, 2, 4, null]]

                    time: O(N) for traversal
                    space: O(h) for recursive stack

        '''

        forest = []
        to_delete_set = set(to_delete)

        def dfs(node):
            # Can make set for constant lookup??
            nonlocal forest, to_delete_set
            if not node:
                return None
            left = dfs(node.left)
            right = dfs(node.right)

            if node.val in to_delete:
                if left is not None:
                    forest.append(left)
                if right is not None:
                    forest.append(right)
                return None
            node.left = left
            node.right = right
            return node
        
        newRoot = dfs(root)
        if newRoot:
            forest.append(newRoot)
        return forest
                
            

        