from utils import *


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []
        self.iter_nodes(root)

    def iter_nodes(self, node: TreeNode):
        while node:
            self.stack.append(node)
            if node.left:
                node = node.left
            else:
                break

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if not self.hasNext():
            return
        node = self.stack.pop()
        val = node.val
        if node.right:
            self.iter_nodes(node.right)
        return val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.stack) > 0:
            return True
        return False


if __name__ == '__main__':
    t = TreeNode(7)
    t3 = TreeNode(3)
    t15 = TreeNode(15)
    t.left = t3
    t.right = t15
    t15.left = TreeNode(9)
    t15.right = TreeNode(20)

    iters = BSTIterator(t)
    print(iters.stack)