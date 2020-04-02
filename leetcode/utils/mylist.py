from typing import TypeVar

T = TypeVar('T', bound="ListNode")


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.__size = 0

    @property
    def size(self):
        return self.__size

    @classmethod
    def of(cls, *nums) -> T:
        if len(nums) == 0:
            return None
        node = ListNode(None)
        ptr = node
        for i in nums:
            n = ListNode(i)
            ptr.next = n
            ptr = ptr.next
        return node.next

    def __str__(self):
        s = []
        ptr = self
        while ptr:
            s.append(ptr.val)
            ptr = ptr.next
        return str(s)


if __name__ == '__main__':
    a = ListNode.of(1, 2, 3)
    print(a)
