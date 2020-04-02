"""
n叉树前序遍历
"""
from typing import *


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        if root.children is None:
            return [root.val]
        res = []
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                for n in node.children[::-1]:
                    stack.append(n)
        return res

    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        if root.children is None:
            return [root.val]
        res = []
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                for n in node.children:
                    stack.append(n)
        return res[::-1]


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n1.children = [n3, n2, n4]
    n3.children = [n5, n6]
    print(Solution().preorder(n1))
    print(Solution().postorder(n1))
