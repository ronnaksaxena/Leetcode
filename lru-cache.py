​
        return node.value
​
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key)
​
        if not node: 
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value
​
            self.cache[key] = newNode
            self._add_node(newNode)
​
            self.size += 1
​
            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update the value.
            node.value = value
            self._move_to_head(node)
        
​
​
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
