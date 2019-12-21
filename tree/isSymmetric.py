"""
给定一个二叉树，检查它是否是镜像对称的。
"""

from tree import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        from collections import deque
        if root is None:
            return True
        queue = deque([root])
        while len(queue) > 0:
            level_result = []
            next_level = deque()
            while len(queue) > 0:
                node = queue.pop()
                if node is None:
                    level_result.append(None)
                    continue
                level_result.append(node.val)
                next_level.appendleft(node.left)
                next_level.appendleft(node.right)
            i, j = 0, len(level_result) - 1
            while i <= j:
                if level_result[i] != level_result[j]:
                    return False
                i += 1
                j -= 1
            queue = next_level
        return True

    def recursion(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, node1: TreeNode, node2: TreeNode) -> bool:
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return node1.val == node2.val and self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)

