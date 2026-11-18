class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = subset = [] Because lists are mutable (can be modified).
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision to NOT include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
        # TC = O(n * 2^n)
        # SC =  O(n)
        # where n = length of nums
        
        