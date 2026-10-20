class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Brute Force Solution
        # n = len(arr)
        # ans = [0] * n
        # for i in range(n):
        #     rightMax = -1
        #     for j in range(i + 1, n):
        #         rightMax = max(rightMax, arr[j])
        #     ans[i] = rightMax
        
        # return ans
        # Time Complexity = O(n^2)
        # Space Complexity = O(n)
        # Auxiliary Space Complexity = O(1) (excluding the output array)

        # Optimal Solution
        rightMax, n = -1, len(arr)
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(rightMax, arr[i])

        return ans
        # Time Complexity = O(n)
        # Space Complexity = O(n)
        # Auxiliary Space Complexity = O(1) (excluding the output array)





                