# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def solve(n, k):
            if not n: # if in null of half leaf node
                return False
            if not (n.right or n.left) and targetSum == k + n.val: # leaf node
                print(k + n.val)
                return True
            return solve(n.left, k + n.val) or solve(n.right, k + n.val)

        return solve(root, 0)
