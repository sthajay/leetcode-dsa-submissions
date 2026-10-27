class Solution:
    def climbStairs(self, n: int) -> int:
        # Dynamic Programming
        one = two = 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one

        # Time Complexity = O(n)
        # Space Complexity = O(1)
        # where n = number of steps
        