# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not (p and q) or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def r(n):
            if not n: return False
            if self.isSameTree(n, q):
                return True
            else:
                return r(n.right) or r(n.left)
        
        return r(root)
