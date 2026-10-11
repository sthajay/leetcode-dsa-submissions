class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    #  Brute Force Solution
        # n, res = len(nums), 0
        # for i in range(n):
        #     cnt = 0
        #     for j in range(i, n):
        #         if nums[j] == 0:
        #             break
        #         cnt += 1
            
        #     res = max(res, cnt)
        
        # return res

    # Time Complexity = O(n^2)
    # Space Complexity = O(1)
    
    # Optimal Solution
        res = cnt = 0
        for n in nums:
            cnt = cnt + 1 if n else 0
            res = max(res, cnt)

        return res
    # Time Complexity = O(n)
    # Space Complexity = O(1)
    