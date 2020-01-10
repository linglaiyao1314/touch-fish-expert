"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""
from utils import *
from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) != len(inorder) or len(preorder) <= 0:
            return
        root = TreeNode(preorder[0])
        pos = inorder.index(preorder[0])
        left_inorder = inorder[:pos]
        right_inorder = inorder[pos+1:]
        if len(left_inorder) > 0:
            root.left = self.buildTree(preorder[1:pos+1], left_inorder)
        if len(right_inorder) > 0:
            root.right = self.buildTree(preorder[pos+1:], right_inorder)
        return root


if __name__ == '__main__':
    t = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(t)
