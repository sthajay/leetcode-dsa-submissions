class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0
        def dfs(r, c):
            if( r < 0 or r >= m or 
                c < 0 or c >= n or
                grid[r][c] != 1
            ):
                return 0
            area = 0
            
            grid[r][c] = 0
            area += 1

            area += dfs(r - 1, c)
            area += dfs(r + 1, c)
            area += dfs(r, c - 1)
            area += dfs(r, c + 1)

            return area
        
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    maxArea = max(dfs(r, c), maxArea)
        
        return maxArea

        # TC = O(m * n)
        # SC = O(m * n)
        # where m = length of rows
        # n = length of columns
            

        