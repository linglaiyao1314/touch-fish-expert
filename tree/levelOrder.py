"""
给定一个二叉树，返回其按层次遍历的节点值
"""

from typing import List
from collections import deque

from tree import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result
        queue = deque([root])
        while len(queue) > 0:
            level_result = []
            next_level = deque()
            while len(queue) > 0:
                node = queue.pop()
                level_result.append(node.val)
                if node.left:
                    next_level.appendleft(node.left)
                if node.right:
                    next_level.appendleft(node.right)
            queue = next_level
            result.append(level_result)
        return result


