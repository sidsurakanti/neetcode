# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def r(n, k):
            if not n:
                return k
            left = r(n.left, k+1)
            right = r(n.right, k+1)
            return max(left, right)
        return r(root, 0)