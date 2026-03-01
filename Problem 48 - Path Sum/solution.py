# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, box):
            if not node:
                return False

            box += node.val

            if not node.left and not node.right:
                return box == targetSum

            return dfs(node.left, box) or dfs(node.right, box)

        return dfs(root, 0)