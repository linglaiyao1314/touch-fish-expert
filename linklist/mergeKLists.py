from linklist import ListNode
from typing import List


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.mergeTwoList(lists[0], lists[1])
        mid = len(lists) // 2
        left_list = lists[:mid]
        right_list = lists[mid:]
        return self.mergeTwoList(self.mergeKLists(left_list), self.mergeKLists(right_list))

    def mergeTwoList(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        ptr = head
        while l1 and l2:
            if l1.val <= l2.val:
                ptr.next = l1
                l1 = l1.next
                ptr = ptr.next
            else:
                ptr.next = l2
                l2 = l2.next
                ptr = ptr.next
        while l1:
            ptr.next = l1
            l1 = l1.next
            ptr = ptr.next
        while l2:
            ptr.next = l2
            l2 = l2.next
            ptr = ptr.next
        return head.next
