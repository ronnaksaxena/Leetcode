'''
Will pop or top be called without any elements in DS? NO

start <=> node <=> end
- top of stack is end.prev

hashTable = {val: node}


maxHeap = [largest -> smallest]




'''
import heapq

class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MaxStack:

    def __init__(self):
        self.start, self.end = ListNode(0), ListNode(0)
        self.start.next, self.end.prev = self.end, self.start
        self.maxHeap = []
        self.nodes = collections.defaultdict(list) # {val: [node]}

    def removeNode(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        del node
        return

    def insertNode(self, node):
        node.prev, node.next = self.end.prev, self.end
        self.end.prev.next = node
        self.end.prev = node
        return
        

    def push(self, x: int) -> None:
        '''
        push - onto max heap
        create Node 
            insert into end of list
            add val: Node to hashtable
        '''
        heapq.heappush(self.maxHeap, -x)
        insertNode = ListNode(x)
        self.nodes[x].append(insertNode)
        self.insertNode(insertNode)
        return None

        

    def pop(self) -> int:
        '''
        Get node from hashtable
        remove node from linked list
        del key from hash table
        '''
        topNode = self.end.prev
        returnVal = topNode.val
        self.nodes[returnVal].pop()
        self.removeNode(topNode)
        return returnVal

    def top(self) -> int:
        return self.end.prev.val
        

    def peekMax(self) -> int:
        '''
        while the top of the heap is not in hash table pop
        '''
        while len(self.nodes[-self.maxHeap[0]]) == 0:
            heapq.heappop(self.maxHeap)
        return -self.maxHeap[0]
        

    def popMax(self) -> int:
        '''
        while top of head is not in hash table delete
        pop from heap and remove from linkedList
        '''
        while len(self.nodes[-self.maxHeap[0]]) == 0:
            heapq.heappop(self.maxHeap)
        valToRemove = -self.maxHeap[0]
        nodeToRemove = self.nodes[valToRemove][-1]
        self.removeNode(nodeToRemove)
        self.nodes[valToRemove].pop()
        return valToRemove
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()