# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = 0
        def calculateSum(root, res):
            if not root:
                return False

            res += root.val
            if res == targetSum and not root.left and not root.right:
                return True

            if calculateSum(root.left, res):
                return True
            
            if calculateSum(root.right, res):
                return True
            
            return False
        
        return calculateSum(root, res)





        

        

        