# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode(0)
        dummy1 = ListNode(0,less)
        greater = ListNode(0)
        dummy2 = ListNode(0,greater)
        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
                
            else:
                greater.next = curr
                greater = greater.next
                
            curr = curr.next
            less.next = None
            greater.next = None
        less.next = dummy2.next.next
        return dummy1.next.next
