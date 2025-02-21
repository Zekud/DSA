# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0,head)
        prev = dummy.next
        curr = head.next
        while curr:
            if prev.val != curr.val:
                prev.next = curr
                prev = curr
            curr= curr.next
        if not curr:
            prev.next = None
        return dummy.next
