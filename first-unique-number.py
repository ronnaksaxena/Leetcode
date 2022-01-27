                    self.tail = newNode
            else:
                if self.vals[num]:
                    #update neighboring points
                    cur = self.vals[num]
                    if cur.prev:
                        cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                    if cur == self.tail:
                        self.tail = cur.prev
                    if cur == self.head:
                        self.head = cur.next
                    self.vals[num] = None
                    del cur
        
​
    def showFirstUnique(self) -> int:
        #print(self.head.val if self.head else -1, self.tail.val if self.tail else -1, self.vals)
        return self.head.val if self.head else -1
        
​
    def add(self, value: int) -> None:
        if value not in self.vals:
                newNode = Node(value)
                self.vals[value] = newNode
                if not self.head:
                    self.head = newNode
                    self.tail = newNode
                else:
                    self.tail.next, newNode.prev = newNode, self.tail
                    self.tail = newNode
        else:
