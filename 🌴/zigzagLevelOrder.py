"""
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

"""
from utils import *
from typing import *

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        queue = [root]
        left_to_right_enqueue = True
        while len(queue) > 0:
            next_level = []
            current_level_res = []
            while len(queue) > 0:
                node = queue.pop()
                if node is None:
                    continue
                current_level_res.append(node.val)
                if left_to_right_enqueue:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                else:
                    if node.right:
                        next_level.append(node.right)
                    if node.left:
                        next_level.append(node.left)
            queue = next_level
            if len(current_level_res) > 0:
                res.append(current_level_res)
            left_to_right_enqueue = not left_to_right_enqueue
        return res


if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    print(Solution().zigzagLevelOrder(node))
