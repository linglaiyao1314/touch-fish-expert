import datetime

print(f"今天是 {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "打印NM呢?这么简单还要打印?"

    def __repr__(self):
        return "我是你打印不了的Tree, 真不是Tree NB!"

    @classmethod
    def make_preorder_traversal(cls, root):
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


    # def print_array(self):
    #


t = TreeNode(3)
t.left = TreeNode(1)
t.right = TreeNode(5)
t.left.left = TreeNode(0)
t.left.right = TreeNode(2)
t.right.left = TreeNode(4)
t.right.right = TreeNode(6)
T1 = t
