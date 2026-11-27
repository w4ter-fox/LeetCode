# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def isMirror(goleft, goright):
            if not goleft and not goright:
                return True
            elif not goleft or not goright:
                return False

            return (goleft.val == goright.val and isMirror(goleft.left, goright.right) and isMirror(goleft.right, goright.left))

        if not root:
            return True

        return isMirror(root.left, root.right)
            
