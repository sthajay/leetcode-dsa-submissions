class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute Force Solution
        # for r in range(len(matrix)):
        #     for c in range(len(matrix[r])):
        #         if matrix[r][c] == target:
        #             return True
        
        # return False
        # # TC = O(m * n) where m = length of rows, and n = length of cols
        # # SC = O(1)

        # Optimal Solution
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + ((r - l) // 2)
            row, col = m // COLS, m % COLS
            if matrix[row][col] > target:
                r = m - 1
            elif matrix[row][col] < target:
                l = m + 1
            else:
                return True
        
        return False
         # # TC = O(log(m * n)) where m = length of rows, and n = length of cols
        # # SC = O(1)
