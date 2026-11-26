# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if root is None:
                return None
            
            lefttail = dfs(root.left)
            righttail = dfs(root.right)

            if lefttail:
                lefttail.right = root.right
                root.right = root.left
                root.left = None

            return righttail or lefttail or root

        dfs(root)