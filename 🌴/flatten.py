"""
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""
from utils import *


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        head = TreeNode(None)
        ptr = head
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node.left = None
            ptr.right = node
            ptr = ptr.right
        return head.right

if __name__ == '__main__':
    t = TreeNode(3)
    t.left = TreeNode(1)
    t.right = TreeNode(5)
    t.left.left = TreeNode(0)
    t.left.right = TreeNode(2)
    t.right.left = TreeNode(4)
    t.right.right = TreeNode(6)
    print(Solution().flatten(t))
