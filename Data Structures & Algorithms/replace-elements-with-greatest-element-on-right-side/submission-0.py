class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #  Brute Force Solution
        n = len(arr)
        ans = [0] * n
        for i in range(n):
            rightMax = -1
            for j in range(i + 1, n):
                rightMax = max(rightMax, arr[j])
            ans[i] = rightMax
        
        return ans
        # Time Complexity = O(n^2)
        # Space Complexity = O(1)
        # The output array is not counted towards space complexity, as the standard convention measures only auxiliary working space.

        # Optimal Solution
        n = len(arr)
        ans = [0] * n
        rightMax = -1
        for i in range(n - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(rightMax, arr[i])
        
        return ans

        #  Time Complexity = O(n)
        # Space Complexity = O(1)



                