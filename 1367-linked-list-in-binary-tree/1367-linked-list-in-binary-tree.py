# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        '''
        input: head:ListNode, root: treeNode
        output: bool

        edge cases:
        if head empty always true
        if root empy and head not empty always false


        Algo:
        helper fn (preorder dfs)
            returns True if path exits or false

        iterate throught root in preorder dfs and check if helper returns true on any nodes

        Time: O(n) n is nodes in tree
        Space: O(h) for recursive stack
        '''

        if not head:
            return True
        if not root and head:
            return False

        def helper(curListNode, curRootNode):
            if not curListNode:
                return True
            if not curRootNode or curRootNode.val != curListNode.val:
                return False
            return helper(curListNode.next, curRootNode.left) or helper(curListNode.next, curRootNode.right)

        def dfs(node):
            if not node:
                return False
            if node.val == head.val and helper(head, node):
                return True

            # prune
            if dfs(node.left):
                return True
            if dfs(node.right):
                return True
            

        return dfs(root)
        