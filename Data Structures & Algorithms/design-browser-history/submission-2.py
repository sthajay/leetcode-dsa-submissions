
# Double Linked List Solution
# class ListNode:
#     def __init__(self, val, prev = None, next = None):
#         self.val = val
#         self.prev = prev
#         self.next = next

# class BrowserHistory:
#     def __init__(self, homepage: str):
#         self.curr = ListNode(homepage)

#     def visit(self, url: str) -> None:
#         self.curr.next = ListNode(url, self.curr)
#         self.curr = self.curr.next # Removing other nodes here

#     def back(self, steps: int) -> str:
#         while self.curr.prev and steps > 0:
#             self.curr = self.curr.prev
#             steps -= 1
        
#         return self.curr.val
        

#     def forward(self, steps: int) -> str:
#         while self.curr.next and steps > 0:
#             self.curr = self.curr.next
#             steps -= 1
        
#         return self.curr.val
        

    # Time Complexity = 
    # Time complexity: O(1) for initialization.
    # Time complexity: O(1) for each visit() function call.
    # Time complexity: O(min(n, steps)) for each back() and forward() function call.

    # Space Complexity = O(m * n)
    # where n = number of visited urls, m = average length of each url, 
    # and steps = number of steps we go forward or back


# Optimal Solution
class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = 0
        self.len = 1
        self.history = [homepage]
        

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr == len(self.history):
            self.history.append(url)
            self.len += 1
        else:
            self.history[self.curr] = url
            self.len = self.curr + 1 # Removing other nodes here 
        

    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]
        
    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.len - 1)
        return self.history[self.curr]

# Time Complexity = 
    # Time complexity: O(1) for initialization.
    # Time complexity: O(1) for each visit() function call.
    # Time complexity: O(1) for each back() and forward() function call.

    # Space Complexity = O(m * n)
    # where n = number of visited urls, m = average length of each url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)