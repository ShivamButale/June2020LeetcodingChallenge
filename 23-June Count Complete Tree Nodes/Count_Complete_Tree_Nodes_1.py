# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):
        if node is None:
            return 0
        else:
            return self.helper(node.left) + self.helper(node.right) + 1
    
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.helper(root)
