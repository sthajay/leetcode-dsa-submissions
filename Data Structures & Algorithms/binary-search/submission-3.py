class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Optimal Solution
        l, r = 0, len(nums) - 1
        while l <= r:
            # (l + r) // 2 can lead to overflow
            m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1 
        # TC = O(logn)
        # SC = O(1)
        # where n = length of nums
        


        # Brute Force Solution
        for i, n in enumerate(nums):
            if n == target:
                return i
        
        return -1
        # TC = O(n)
        # SC = O(1)
        # where n = length of nums
        