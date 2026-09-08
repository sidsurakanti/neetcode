# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = None
        
        def r(n):
            nonlocal lca
            if not n:
                return (False, False)

            (fx, fy) = r(n.right) # found from right
            (fa, fb) = r(n.left) # found from left

            x = (fa or fx or n.val == p.val)
            y = (fy or fb or n.val == q.val)
            if x and y and not lca: # set lca first time we find both p and q
                lca = n
            
            return (x, y)
        
        r(root)
        return lca
        