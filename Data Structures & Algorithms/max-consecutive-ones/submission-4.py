class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Optimal Solution
        res = cnt = 0
        for n in nums:
            cnt = cnt + 1 if n else 0
            res = max(res, cnt)
        
        return res
        # TC = O(n)
        # SC = O(1)
        # where n = length of nums


        # Brute Force Solution
        n = len(nums)
        res = 0
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] == 1:
                    cnt += 1
                else:
                    break
            res = max(res, cnt)
        
        return res
        # TC = O(n^2)
        # SC = O(1)
        # where n = length of nums
            


        















