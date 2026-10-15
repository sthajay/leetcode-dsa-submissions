class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Brute Force Solution
        # stack = []
        # for n in operations:
        #     if n == 'C':
        #         stack.pop()
        #     elif n == 'D':
        #         stack.append(2 * stack[-1])
        #     elif n == '+':
        #         stack.append(stack[-1] + stack[-2])
        #     else:
        #         stack.append(int(n))
        
        # return sum(stack)
        # Time Complexity = O(n)
        # Space Complexity = O(n)

        # Optimal Solution
        stack,res = [], 0
        for n in operations:
            if n == '+':
                res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif n == 'C':
                res -= stack.pop()
            elif n == 'D':
                res += (2 * stack[-1])
                stack.append(2 * stack[-1])
            else: 
                res += int(n)
                stack.append(int(n))
        
        return res
        # Time Complexity = O(n)
        # Space Complexity = O(n)

