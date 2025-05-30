"""# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')

        def in_order(node):
            if not node:
                return
            in_order(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            in_order(node.right)

        in_order(root)
        return self.min_diff
"""

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        values = []

        def dfs(node):
            if not node:
                return
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        values.sort()

        min_diff = float('inf')
        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i] - values[i - 1])

        return min_diff
