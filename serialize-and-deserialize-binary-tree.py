        
        
        
​
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def helper(l):
            if l[0] == 'None':
                l.pop(0)
                return None
            else:
                root = TreeNode(l[0])
                l.pop(0)
                root.left = helper(l)
                root.right = helper(l)
                return root
            
        valList = data.split(',')
        return helper(valList)
        
​
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
