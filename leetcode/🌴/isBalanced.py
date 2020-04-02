"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

 

限制：
1 <= 树的结点个数 <= 10000

"""
from leetcode.utils import *

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        diff = abs(left_depth - right_depth)
        return self.isBalanced(root.left) and self.isBalanced(root.right) and (diff <= 1)

    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max([1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right)])
