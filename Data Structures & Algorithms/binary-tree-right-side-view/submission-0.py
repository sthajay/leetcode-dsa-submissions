# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Optimal Solution - Remove level
        res = []
        q = deque()
        if root:
            q.append(root)
        
        while q:
            lenQ = len(q)
            for i in range(lenQ):
                cur = q.popleft()
                if i == lenQ - 1:
                    res.append(cur.val)
                
                if cur.left:
                    q.append(cur.left)
                
                if cur.right:
                    q.append(cur.right)
            
        return res



        # Brute Force - Similar to Binary Tree Level Order Traversal
        res = []
        q = deque()
        if root:
            q.append(root)
        level = 0
        while q:
            lenQ = len(q)
            res.append([])
            for _ in range(lenQ):
                cur = q.popleft()
                res[level].append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            level += 1
        
        return [n[-1] for n in res]
        # TC = O(n)
        # SC = O(n)
        # where n = number of nodes
        