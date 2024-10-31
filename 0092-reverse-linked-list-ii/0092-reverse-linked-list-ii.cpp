/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
 /*
 left = 2, right = 4

 [1,2,3,4,5],
  p  l    r

- p is before l
- move l and p, l times
- move r (diff + 1) times

reverserse l -> r
point p next to l
return head
    4 -> 3 -> 2 -> Null

 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* leftBound = dummy;

        ListNode* l = head;
        ListNode* r = head;
        // Move ptrs along to left
        for (int i = 1; i < left; i++) {
            leftBound = leftBound->next;
            l = l->next;
            r = r->next;
        }
        // leftBound points to node before start of rev
        // need to move r to node after its boundary
        int diff = right - left;
        for (int i = 0; i < (diff+1); i++) {
            r = r->next;
        }
        //. 1 -> 2 -> 3 -> 4 -> 5 ->
        //  p.   l.             r
        
        // reverse section
        ListNode* newHead = nullptr;
        ListNode* newTail = l;
        while (l != r) {
            ListNode* temp = l->next;
            l->next = newHead;
            newHead = l;
            l = temp;
        }

        // rejoin ends if not null
        if (leftBound) {
            leftBound->next = newHead;
        }
        if (r) {
            newTail->next = r;
        }


        return dummy->next;
        
    }
};