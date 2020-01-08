"""给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
"""

from tree import *
from typing import List

from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = deque()
        stack = deque([root])
        while len(stack) > 0:
            current_level = []
            next_level = deque()
            while len(stack) > 0:
                node = stack.pop()
                if node is None:
                    continue
                current_level.append(node.val)
                if node.left:
                    next_level.appendleft(node.left)
                if node.right:
                    next_level.appendleft(node.right)
            stack = deque(next_level)
            res.appendleft(current_level)
        return list(res)


if __name__ == '__main__':
    print(Solution().levelOrderBottom(T1))
