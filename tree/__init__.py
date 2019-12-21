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

