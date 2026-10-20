# [0, 1, 2, 3]
# [3, 2, 1, 0]
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative Approach
        # prev, curr = None, head
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        
        # return prev

        # Time Complexity = O(n)
        # Space Complexity = O(1)

        # Recursive Approach
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        
        head.next = None
        return newHead

        # Time Complexity = O(n)
        # Space Complexity = O(n)


        