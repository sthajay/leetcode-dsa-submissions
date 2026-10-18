# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [0, 1, 2, 3]
# [3, 2, 1, 0]
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative approach
        prev, curr = None, head
        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev


        