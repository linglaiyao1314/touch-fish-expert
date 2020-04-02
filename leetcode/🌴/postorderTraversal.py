"""给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
"""

from leetcode.utils import *
from typing import List


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """相当于左右子树对调后，进行前序遍历，最终结果反转"""
        result = []
        if root is None:
            return result
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]


if __name__ == '__main__':
    print(Solution().postorderTraversal(T1))