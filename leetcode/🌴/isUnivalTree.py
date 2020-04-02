"""
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
"""

from leetcode.utils import *


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.find(root, root.val)

    def find(self, node, val):
        if node is None:
            return True
        if node.val != val:
            return False
        return self.find(node.left, val) and self.find(node.right, val)