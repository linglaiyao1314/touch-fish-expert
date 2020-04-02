"""
返回与给定先序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。
"""
from utils import *
from typing import *


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        for num in preorder[1:]:
            self.insert(root, num)
        return root

    def insert(self, root, val):
        ptr = root
        while ptr:
            if val < ptr.val:
                if ptr.left is None:
                    ptr.left = TreeNode(val)
                    return
                ptr = ptr.left
            elif val > ptr.val:
                if ptr.right is None:
                    ptr.right = TreeNode(val)
                    return
                ptr = ptr.right

