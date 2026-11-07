class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute Force Solution
        for i, n in enumerate(nums):
            if n == target:
                return i
        
        return -1
        # TC = O(n)
        # SC = O(1)
        # where n = length of nums
        