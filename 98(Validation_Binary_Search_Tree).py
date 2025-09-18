# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if node is None:
#             return True
#         if not limit[0]<node.val<limit[1]:
#             return False
#         left=self.solve(node.left,[limit[0],node>val])
#         if left==False:
#             return False
#         right=self.solve(node.right,[node.val,limit[1]])
#         return left and right
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         return self.solve(root, [float("-inf"), float("inf")])

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, node: Optional[TreeNode], limit: list) -> bool:
        if node is None:
            return True
        if not limit[0] < node.val < limit[1]:
            return False
        left = self.solve(node.left, [limit[0], node.val])
        if not left:
            return False
        right = self.solve(node.right, [node.val, limit[1]])
        return right  # left is already True if we reach here

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.solve(root, [float("-inf"), float("inf")])
