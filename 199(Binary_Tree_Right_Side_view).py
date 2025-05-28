"""# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        result = []

        if root is None:
            return result

        queue.append(root)
        while len(queue) != 0:
            level_size = len(queue)
            for i in range(level_size):
                root = queue.popleft()
                if i == level_size - 1:
                    result.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        return result
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def reversepostorder(node, level, ans):
            if node is None:
                return 
            if len(ans) == level:
                ans.append(node.val)
            if node.right:
                reversepostorder(node.right, level + 1, ans)
            if node.left:
                reversepostorder(node.left, level + 1, ans)
        
        ans = []
        reversepostorder(root, 0, ans)
        return ans
