class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None
        
class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
       
    def get(self, index: int) -> int:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and curr != self.tail and index == 0:
            return curr.val
        
        return -1
        

    def addAtHead(self, val: int) -> None:
        prev, node, next = self.head, ListNode(val), self.head.next
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev  

    def addAtTail(self, val: int) -> None:
        prev, node, next = self.tail.prev, ListNode(val), self.tail
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
     
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and index == 0:
            prev, node, next = curr.prev, ListNode(val), curr
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev
        
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and curr != self.tail and index == 0:
            prev, next = curr.prev, curr.next
            prev.next = next
            next.prev = prev
      
        # - Time complexity:
        #   - O(1) for initialization.
        #   - O(1) for addAtHead() and addAtTail().
        #   - O(n) for get(), addAtIndex(), and deleteAtIndex().
        # - Space complexity: O(n) for storing n nodes in the linked list.

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)