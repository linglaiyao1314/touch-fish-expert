"""
给定一个二叉树，找出其最大深度。
"""


from tree import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max([self.maxDepth(root.left), self.maxDepth(root.right)])
