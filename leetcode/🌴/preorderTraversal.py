"""
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]

"""
from leetcode.utils import *
from typing import List


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # res = []
        # self.recursion(root, res)
        # return res
        result = []
        if root is None:
            return result
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def recursion(self, node: TreeNode, res):
        if node is None:
            return
        res.append(node.val)
        if node.left:
            self.recursion(node.left, res)
        if node.right:
            self.recursion(node.right, res)
        return


if __name__ == '__main__':
    print(Solution().preorderTraversal(T1))