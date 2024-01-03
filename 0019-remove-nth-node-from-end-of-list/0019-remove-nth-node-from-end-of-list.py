# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        curr = head
        size=0
        while curr:
            size+=1
            curr = curr.next
        i= size-n
        j=0
        item = ListNode() #dummyNode
        item.next = head
        while j<i:
            j+=1
            item = item.next
        nextNode=item.next
        item.next = nextNode.next
        nextNode.next = None
        return head if i!=0 else item.next
            