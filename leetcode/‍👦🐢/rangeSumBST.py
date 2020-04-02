"""
给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。

二叉搜索树保证具有唯一的值。

示例 1：

     10
    5  15
  3  7    18
输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
输出：32
示例 2：

输入：root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
输出：23
     10
   5   15
 3  7  13 18
1  6
"""

from leetcode.utils import *


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0
        if L > root.val and R > root.val:
            return self.rangeSumBST(root.right, L, R)
        if L < root.val and R < root.val:
            return self.rangeSumBST(root.left, L, R)
        return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)


if __name__ == '__main__':
    t = TreeNode(10)
    t.left = TreeNode(5)
    t.right = TreeNode(15)
    t.left.left = TreeNode(3)
    t.left.right = TreeNode(7)
    t.left.right.left = TreeNode(6)
    t.right.right = TreeNode(18)
    print(Solution().rangeSumBST(t, 6, 10))
