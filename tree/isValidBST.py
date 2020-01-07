"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

[10,5,15,null,null,6,20]
   10
  5  15
    6  20

   3
  1 5
 0 2 4 6
"""
from tree import *


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = []
        self.iter_left(root, stack)
        last_val = None
        while len(stack) > 0:
            node = stack.pop()
            if last_val is None:
                last_val = node.val
            else:
                if last_val < node.val:
                    last_val = node.val
                else:
                    return False
            if node.right:
                self.iter_left(node.right, stack)
        return True

    def iter_left(self, node: TreeNode, stack):
        while node:
            stack.append(node)
            node = node.left


if __name__ == '__main__':
    t = TreeNode(3)
    t.left = TreeNode(1)
    t.right = TreeNode(5)
    t.left.left = TreeNode(0)
    t.left.right = TreeNode(2)
    t.right.left = TreeNode(4)
    t.right.right = TreeNode(6)
    print(Solution().isValidBST(t))