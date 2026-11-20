class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res




















































        # res = subset = [] Because lists are mutable (can be modified).
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                # Save a copy because backtracking modifies the same subset list.
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
        # SC = O(n) auxiliary space (recursion + subset)
        #    = O(n * 2^n) including output
        # where n = length of nums
        
        # Decision Tree for nums = [1, 2, 3]
        #
        #                         []
        #                   /            \
        #                [1]              []
        #              /     \          /    \
        #          [1,2]     [1]      [2]     []
        #          /   \     /  \     /  \    /  \
        #     [1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] []
        #
        # Left branch  = Include current number
        # Right branch = Exclude current number
        # Each leaf represents one subset.
        # Total subsets = 2^n

        # Auxiliary space = Extra working memory used by the algorithm.
        # Total space = Auxiliary space + output storage.