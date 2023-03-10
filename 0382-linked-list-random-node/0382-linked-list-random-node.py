# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.n = 0
        self.head = head
        ptr = self.head
        while ptr:
            self.n += 1
            ptr = ptr.next
        

    def getRandom(self) -> int:
        i = random.randint(0, self.n-1)
        ret = self.head
        for _ in range(i):
            ret = ret.next
            
        return ret.val
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()