"""
设计链表的实现。您可以选择使用单链表或双链表。
单链表中的节点应该具有两个属性：val和next。val是当前节点的值，
next是指向下一个节点的指针/引用。如果要使用双向链表，
则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。
在链表类中实现这些功能：

get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。
如果 index 等于链表的长度，则该节点将附加到链表的末尾。
如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引index 有效，则删除链表中的第index 个节点。
 

示例：

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
linkedList.get(1);            //返回2
linkedList.deleteAtIndex(1);  //现在链表是1-> 3
linkedList.get(1);            //返回3
 
提示：
所有val值都在 [1, 1000] 之内。
操作次数将在  [1, 1000] 之内。
请不要使用内置的 LinkedList 库。
"""


class LinkedNode:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt

    def __eq__(self, other):
        return self.val == other.val and self.prev == self.prev and self.next == self.next

    def __str__(self):
        return str(self.val)


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sentinel = LinkedNode(None)
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.size:
            return -1
        ptr = self.sentinel
        while index >= 0:
            ptr = ptr.next
            index -= 1
        return ptr.val

    def getNode(self, index) -> LinkedNode:
        if index >= self.size:
            return None
        ptr = self.sentinel
        while index >= 0:
            ptr = ptr.next
            index -= 1
        return ptr

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = LinkedNode(val)
        if self.isEmpty():
            self.sentinel.next = new_node
            new_node.next = new_node
            new_node.prev = new_node
            self.size += 1
            return
        self.size += 1
        old_first_node = self.sentinel.next
        new_node.prev = old_first_node.prev
        new_node.next = old_first_node
        old_first_node.prev.next = new_node
        old_first_node.prev = new_node
        self.sentinel.next = new_node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.isEmpty():
            self.addAtHead(val)
            return
        self.size += 1
        new_node = LinkedNode(val)
        old_last_node = self.sentinel.next.prev
        new_node.prev = old_last_node
        new_node.next = old_last_node.next
        old_last_node.next.prev = new_node
        old_last_node.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list,
        the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            self.size += 1
            node = self.getNode(index)
            new_node = LinkedNode(val)
            new_node.next = node
            new_node.prev = node.prev
            node.prev.next = new_node
            node.prev = new_node




    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        node = self.getNode(index)
        if node is None:
            return None
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
        if index == 0:
            self.sentinel.next = next_node


    def isEmpty(self):
        return self.size == 0

    def __str__(self):
        if self.size == 0:
            return "[]"
        res = []
        ptr = self.sentinel.next
        size = self.size
        while size > 0:
            res.append(ptr.val)
            ptr = ptr.next
            size -= 1
        return str(res)


if __name__ == '__main__':
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)
    linkedList.addAtTail(3)
    linkedList.addAtIndex(1, 2)
    print(linkedList)
    print(linkedList.get(1))
    linkedList.deleteAtIndex(0)
    print(linkedList)
    print(linkedList.get(0))