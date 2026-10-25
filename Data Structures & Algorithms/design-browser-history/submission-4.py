# Optimal Solution
class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = 0
        self.n = 1
        self.history = [homepage]
     
    def visit(self, url: str) -> None:
        self.cur += 1
        if self.cur == len(self.history):
            self.history.append(url)
            self.n += 1
        else:
            self.history[self.cur] = url
            self.n = self.cur + 1
            
    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]
       
    def forward(self, steps: int) -> str:
        self.cur = min(self.n - 1, self.cur + steps)
        return self.history[self.cur]

    # Time Complexity = 
    # Time complexity: O(1) for initialization.
    # Time complexity: O(1) for each visit() function call.
    # Time complexity: O(1) for each back() and forward() function call.

    # Space Complexity = O(m * n)
    # where n = number of visited urls, m = average length of each url

# Double Linked List - Brute Force Solution
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
#         self.curr = self.curr.next
        
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

    # Time complexity: O(1) for initialization.
    # Time complexity: O(1) for each visit() function call.
    # Time complexity: O(min(n, steps)) for each back() and forward() function call.

    # Space Complexity = O(m * n)
    # where n = number of visited urls, m = average length of each url, 
    # and steps = number of steps we go forward or back
      
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)