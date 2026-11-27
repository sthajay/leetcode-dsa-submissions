class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        originalColor = image[sr][sc]

        if originalColor == color:
            return image
        
        def dfs(r, c):
            if (r >= m or r < 0 or
                c >= n or c < 0 or
                image[r][c] != originalColor
            ):
                return
            
            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        
        dfs(sr, sc)
        return image
            

















































        m, n = len(image), len(image[0])
        originalColor = image[sr][sc]


        if originalColor == color:
            return image

        def dfs(r, c):
            if (
                r >= m or r < 0 or
                c >= n or c < 0 or
                image[r][c] != originalColor
            ):
                return
            
            image[r][c] = color

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        dfs(sr, sc)

        return image

        # TC = O(m * n)
        # SC = O(m * n) 
        # where m = length of rows 
        # n = length of columns
            

        