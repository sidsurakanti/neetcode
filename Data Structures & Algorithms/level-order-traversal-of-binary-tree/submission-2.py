# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []

        while q:
            # process level
            a = []
            for _ in range(len(q)):
                n = q.popleft() # remove node from q
                if not n: continue
                # process node
                a.append(n.val)
                q.extend([n.left, n.right])
            res.append(a)

        return res[:-1]


            