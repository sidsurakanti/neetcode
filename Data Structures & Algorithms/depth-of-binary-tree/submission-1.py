# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, n: Optional[TreeNode]) -> int:
        if not n:
            return 0
        l = self.maxDepth(n.left)
        r = self.maxDepth(n.right)
        return 1 + max(l, r)