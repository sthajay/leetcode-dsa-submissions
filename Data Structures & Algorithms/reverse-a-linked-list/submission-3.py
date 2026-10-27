class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive Approach
        # if not head:
        #     return None
        
        # newHead = head
        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head
        
        # head.next = None

        # return newHead
        # TC = O(n)
        # SC = O(n) where n = length of linked list

        # Iterative Solution - Optimal Solution
        cur, prev = head, None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
        # TC = O(n)
        # SC = O(1) where n = length of linked list
        

       