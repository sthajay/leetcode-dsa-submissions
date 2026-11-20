class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            # Include nums[i]: stay at i because the same number can be reused.
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # Exclude nums[i]: move to i + 1 to try the next number.
            cur.pop()
            dfs(i + 1, cur, total)
            # Unlike Subsets (i + 1 in both), Combination Sum allows reusing numbers.

        dfs(0, [], 0)
        return res
        
        # TC = O(N * 2^(T/M)) - Backtracking explores combinations.
        # SC = O(T/M) - Recursion stack and current combination.
        # N = len(nums), T = target, M = min(nums)
        
        