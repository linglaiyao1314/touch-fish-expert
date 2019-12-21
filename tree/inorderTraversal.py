"""
给定一个二叉树，返回它的中序遍历。
"""
from typing import List
from tree import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result
        stack = []
        self.iter_left(root, stack)
        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                self.iter_left(node.right, stack)
        return result

    def iter_left(self, node: TreeNode, stack: List[TreeNode]):
        while node:
            stack.append(node)
            node = node.left

    def recursion(self, root:TreeNode):
        if root is None:
            return []
        result = []
        if root.left:
            result.extend(self.recursion(root.left))
        result.append(root.val)
        if root.right:
            result.extend(self.recursion(root.right))
        return result


