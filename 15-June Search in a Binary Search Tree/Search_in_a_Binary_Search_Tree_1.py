# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while True:
            if not root:
                return None
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            elif root.val > val:
                root = root.left
