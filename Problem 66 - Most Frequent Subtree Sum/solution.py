# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            s = node.val + left + right

            freq[s] += 1

            return s

        dfs(root)

        max_freq = max(freq.values())

        res = []

        for k, v in freq.items():
            if v == max_freq:
                res.append(k)

        return res