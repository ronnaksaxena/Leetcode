# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        '''
        iterate through all nodes and count how many times value appears
        iterate through list and remove nodes that appear >= 2 times
        
        cnt = {1: 1,
                2: 2,
                3: 1}
        d -> 1 -> 2 -> 3 -> 2
             p
                  c
        while cur:
            if cnt[c] > 1: remove
            else: traverse next
            p.next = p.next.next
            del cur
            cur = p.next
        time: O(n) traverse nodes twice
        spcace: O(n): to store frequencies of all nodes
        '''
        # Init counter
        cnt = collections.defaultdict(int)
        cur = head
        while cur:
            cnt[cur.val] += 1
            cur = cur.next
        # Modify list
        dummy = ListNode(0,head)
        prev, cur = dummy, head
        while cur:
            # Remove
            if cnt[cur.val] > 1:
                prev.next = prev.next.next
                del cur
                cur = prev.next
            # Keep
            else:
                prev, cur = cur, cur.next
        return dummy.next
                
                
        
        