# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative Approach (Optimal)
        # dummy = node = ListNode()
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         node.next = list1
        #         list1 = list1.next
        #     else:
        #         node.next = list2
        #         list2 = list2.next
        #     node = node.next
        
        # node.next = list1 or list2

        # return dummy.next

        # Time Complexity = O(n + m)
        #   where n = length of list1 and m = length of list2
        # Space Complexity = O(1), as we reuse existing nodes without creating new ones (except the dummy node).

        # Recursive Approach
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

        # Time Complexity = O(n + m)
        # Space Complexity = O(n + m)

