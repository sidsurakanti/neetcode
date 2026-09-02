# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def r(node, lvl):
            if not node:
                return (1, lvl)
            
            Lbal, left_height = r(node.left, lvl + 1)
            Rbal, right_height = r(node.right, lvl + 1)
            # print(left_height, right_height)

            if not (Lbal and Rbal):
                # notBal seen
                return (0, -10000)
            elif abs(left_height - right_height) > 1:
                # notBal found
                return (0, -10000)
            else:
                return (1, max(left_height, right_height))


            
        # print(r(root, 0))
        return [False, True][r(root, 0)[0]]

            