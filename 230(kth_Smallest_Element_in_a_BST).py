# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        curr = root
        while curr:
            if not curr.left:
                count += 1
                if count == k:
                    return curr.val  # ✅ use val instead of data
                curr = curr.right
            else:
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right
                if not pre.right:
                    pre.right = curr
                    curr = curr.left  # ✅ move to left subtree after threading
                else:
                    pre.right = None
                    count += 1
                    if count == k:
                        return curr.val  # ✅ use val instead of data
                    curr = curr.right
        return -1
