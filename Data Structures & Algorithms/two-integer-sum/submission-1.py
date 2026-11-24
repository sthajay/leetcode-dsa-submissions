class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Optimal Solution
        cnt = {}
        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in cnt:
                return [cnt[diff], i]
            
            cnt[diff] = i
        
            








        # Brute Force Solution
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                

        # TC = O(n^2)
        # SC = O(1)
        # where n = length of nums

        