from leetcode.utils import *


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        res = None
        ptr = head
        while ptr:
            current = ptr
            ptr = ptr.next
            current.next = res
            res = current
        return res

    def reverseRecursion(self, head: ListNode):
        if head is None:
            return head
        tail = head.next
        reverse_tail = self.reverseRecursion(tail)
        if reverse_tail is None:
            return head
        tail.next = head
        head.next = None
        return reverse_tail


if __name__ == '__main__':
    print(Solution().reverseList(ListNode.of(1, 2, 3, 4, 5)))
    print(Solution().reverseRecursion(ListNode.of(1, 2)))
