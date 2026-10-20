class MinStack: 
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # if not self.stack:
        #     minm = val
        # else:
        #     minm = min(val, self.stack[-1][1])

        minm = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, minm))

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]

    # Time Complexity = O(1) per operation
    # Space Complexity = O(n)
    # Auxiliary Space Complexity = O(n)
