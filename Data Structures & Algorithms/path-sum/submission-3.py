# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def calculateSum(root, targetSum):
            if not root:
                return False
            
            targetSum -= root.val

            if targetSum == 0 and not root.right and not root.left:
                return True
            
        
            return calculateSum(root.left, targetSum) or calculateSum(root.right, targetSum) 
        
        return calculateSum(root, targetSum)

    # TC = O(n)
    # SC = O(n)
    # where n = no. of nodes