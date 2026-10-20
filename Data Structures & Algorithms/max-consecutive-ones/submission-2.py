class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Brute Force Solution
        # n, res = len(nums), 0
        # for i in range(n):
        #     count = 0
        #     for j in range(i, n):
        #         if nums[j] == 1:
        #             count += 1
        #         else: break
        #     res = max(res, count)
        
        # return res
        # Time Complexity = O(n^2)
        # Space Complexity = O(1)

        # Optimal Solution
        res = count = 0
        for n in nums:
            count = count + 1 if n else 0
            res = max(res, count)
        
        return res

        # Time Complexity = O(n)
        # Space Complexity = O(1)
            
        















