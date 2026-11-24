class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Optimal Solution
        cnt = {}
        for n in nums:
            if n not in cnt:
                cnt[n] = 1
            else:
                return True
        
        return False

        # Brute Force Solution
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        
        return False

        # TC = O(n^2)
        # SC = O(1)
        # where n = length of nums

        