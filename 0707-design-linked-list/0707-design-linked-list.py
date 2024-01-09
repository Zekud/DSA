class ListNode:
    def __init__(self,val):
        self.prev = None
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1) #dummy Node
        self.tail = ListNode(-1) #dummy Node
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        i=0
        start = self.head.next
        while i<index and start != self.tail:
            start = start.next
            i+=1
        return start.val if start != self.tail else -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.prev = self.tail.prev
        newNode.next = self.tail
        self.tail.prev.next = newNode
        self.tail.prev = newNode

    def addAtIndex(self, index: int, val: int) -> None: 
        i=0
        start = self.head.next
        while start!=self.tail:
            i+=1
            start = start.next
        if index > i:
            return
        else:
            newNode= ListNode(val)
            j=0
            start = self.head.next
            while j<index and start != self.tail:
                start = start.next
                j+=1
            newNode.next = start
            newNode.prev = start.prev
            start.prev.next = newNode
            start.prev = newNode

    def deleteAtIndex(self, index: int) -> None:
        i=0
        start = self.head.next
        while start!=self.tail:
            i+=1
            start = start.next
        if index >= i:
            return
        else:
            j=0
            start = self.head.next
            while j<index and start != self.tail:
                start = start.next
                j+=1
            start.prev.next =start.next
            start.next.prev = start.prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)