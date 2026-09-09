# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# we can observe that each good node is basically
# just every max node encountered throughout the branch so far

# we can solve this by simply just passing down the max node encountered and if we encounter
# a val >= max_so_far

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def r(n, k):
            nonlocal count
            if not n: return

            if (kp := n.val) >= k:
                count += 1
                return r(n.right, kp), r(n.left, kp)
            return r(n.right, k), r(n.left, k)
        
        r(root, -200)
        return count

        