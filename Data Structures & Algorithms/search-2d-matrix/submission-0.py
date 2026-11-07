class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute Force Solution
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == target:
                    return True
        
        return False
        # TC = O(m * n)
        # SC = O(1)
        # where m = no. of rows and 
        # n = no. of columns of a matrix

        
        