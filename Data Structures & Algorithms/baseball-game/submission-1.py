class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Brute Force Solution
        # stack = []
        # for op in operations:
        #     if op == '+':
        #         stack.append(stack[-1] + stack[-2])
        #     elif op == 'C':
        #         stack.pop()
        #     elif op == 'D':
        #         stack.append(stack[-1] * 2)
        #     else:
        #         stack.append(int(op))
        
        # return sum(stack)

        # Time Complexity = O(n)
        # Space Complexity = O(n)
        
        # Optimal Solution
        stack, ans = [], 0
        for op in operations:
            if op == '+':
                ans += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                ans -= stack.pop()
            elif op == 'D':
                ans += stack[-1] * 2
                stack.append(stack[-1] * 2)
            else:
                ans += int(op)
                stack.append(int(op))
        
        return ans
        # Time Complexity = O(n)
        # Space Complexity = O(n)

