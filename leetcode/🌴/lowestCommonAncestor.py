"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
"""

from leetcode.utils import *


class Solution:
    def lowestCommonAncestorBST(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        if p == q:
            return p
        val = root.val
        # 处于不同子树时，目标达成
        if p.val <= val and q.val <= val:
            return self.lowestCommonAncestorBST(root.left, p, q)
        elif p.val >= val and q.val >= val:
            return self.lowestCommonAncestorBST(root.right, p, q)
        else:
            return root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        if root is None:
            return None
        if root == p or root == q:
            return root
        if p == q:
            return p
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
