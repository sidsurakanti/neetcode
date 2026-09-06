# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# we can first start by observing that at each edge node the max path would be 0 
# one level above that we would a subroot with max path: 1 + sum((left_max, right_max)) 
# another level above that we can guarantee that the max path would be: 1 + sum(biggest_left_or_right_FROM_{left, right}) 

# fromt his we can derive that the simple solutino tot his problem is: 
# 1: recurse down the tree 
# 2: calculate max path from formula (1 + sum(left_max, right_max))
# 3: return max path of left subtree, right subtree

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxP = 0

        def r(n):
            nonlocal maxP

            if not n:
                return 0
            
            left_max = r(n.left)
            right_max = r(n.right)
            # print('lm, rm:', left_max, right_max)

            m = 1 + sum((left_max, right_max))
            # print('m:', m, n.val)
            maxP = max(m, maxP)

            return max(left_max + 1, right_max + 1)

        r(root)
        return maxP - 1
