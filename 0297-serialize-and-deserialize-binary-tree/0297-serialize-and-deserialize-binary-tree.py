# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
            1
          /    \
        2       3
     /.   \    /   \
     n     n   4   5
                /\ /\
                n n n n

    "1, 2, Null, Null, 3, 4, null, null, 5, null, null'


    (1)
   /.   \
   (2)  (3)
   / \.         /. \
  null null.   (4.) (5)
            /   \   /   \
            null null null null

            serialize
            preorder + concat

            deseralize
            convert string to list
            build new tree in preorder

            time complexity of O(N) where n is numbe of nodes
            space: complexity of O(H) where h is height of tree for recursive stack
'''
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            return [str(node.val)] + dfs(node.left) + dfs(node.right) if node else ['null']
        
        return ','.join(dfs(root))

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        def dfs(data):
            if not data:
                return None
            nodeVal = data.pop(0)
            if nodeVal == 'null':
                return None
            root = TreeNode(nodeVal)
            root.left = dfs(data)
            root.right = dfs(data)
            return root

        return dfs(data)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))