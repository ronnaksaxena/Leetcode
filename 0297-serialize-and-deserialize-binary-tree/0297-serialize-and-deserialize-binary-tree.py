# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preOrder(node):
            return str(node.val) + ',' + preOrder(node.left) + preOrder(node.right) if node else 'None,'
        
        return preOrder(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        def dfs(nodes):
            cur = vals.pop(0)
            if cur == 'None':
                return None
            root = TreeNode(int(cur))
            root.left = dfs(nodes)
            root.right = dfs(nodes)
            return root
        
        return dfs(vals)
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))