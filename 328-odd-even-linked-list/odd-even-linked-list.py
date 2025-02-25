# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev,curr = head,head.next
        dummy = ListNode(0,prev)
        dummy2 = ListNode(0,curr)
        
        while curr and curr.next:
            prev.next = prev.next.next
            curr.next = curr.next.next
            prev = prev.next
            curr = curr.next
        prev.next = dummy2.next
        return dummy.next