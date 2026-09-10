# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, n: Optional[TreeNode]) -> bool:
        o = []
        def r(n):
            if not n: return
            r(n.left)
            o.append(n.val)
            r(n.right)

        r(n)
        # print(o)

        i, l = 1, len(o)
        while i < l and o[i - 1] < o[i]:
            i += 1
        return False if i < l else True


        