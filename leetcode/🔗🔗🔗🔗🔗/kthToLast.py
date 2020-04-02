"""
实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。

注意：本题相对原题稍作改动

示例：

输入： 1->2->3->4->5 和 k = 2
输出： 4
说明：
n - k + 1
给定的 k 保证是有效的。
"""

from leetcode.utils import *


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        root = ListNode(None)
        root.next = head
        slow = root
        fast = root
        while k > 0 and fast:
            fast = fast.next
            k -= 1
        while fast is not None:
            slow = slow.next
            fast = fast.next
        return slow.val


if __name__ == '__main__':
    x = ListNode.make([1])
    print(Solution().kthToLast(x, 1))
