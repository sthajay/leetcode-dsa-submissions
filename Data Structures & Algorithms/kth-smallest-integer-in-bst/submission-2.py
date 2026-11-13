# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Use this
        stack = []
        cur = root
        cnt = 0
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            k -= 0
            if k == 0:
                return cur.val
            
            cur = cur.right
        # TC: O(h + k), O(n) in the worst case.
        # SC: O(h), where h is the height of the tree.

        # My Solution
        stack = []
        cnt = 0
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()

            cnt += 1
            if cnt == k:
                return cur.val

            cur = cur.right

        # TC: O(h + k), O(n) in the worst case.
        # SC: O(h), where h is the height of the tree.
         