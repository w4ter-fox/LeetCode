# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def depth_dfs(node):
            nonlocal max_diameter
            if not node:
                return 0

            leftdepth = depth_dfs(node.left)
            rightdepth = depth_dfs(node.right)

            max_diameter = max(max_diameter, leftdepth + rightdepth)

            return max(leftdepth, rightdepth) + 1

        depth_dfs(root)
        return max_diameter