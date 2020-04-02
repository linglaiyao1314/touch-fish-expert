"""
给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
 

限制：

1 ≤ k ≤ 二叉搜索树元素个数
"""

from utils import *

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        stack = []
        self.iter_nodes(root, stack)
        while len(stack) > 0:
            k -= 1
            node = stack.pop()
            if k == 0:
                return node.val
            if node.left:
                self.iter_nodes(node.left, stack)

    def iter_nodes(self, node: TreeNode, stack):
        """反向迭代,每次最大元素入栈"""
        while node:
            stack.append(node)
            if node.right:
                node = node.right
            else:
                break
