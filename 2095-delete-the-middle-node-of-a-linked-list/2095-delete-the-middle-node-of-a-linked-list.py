# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        prev = ListNode() #dummy Node
        slow,fast = head, head
        prev.next = slow
        tracker = prev
        if prev.next.next == None:
            return None
            
        while fast and fast.next:
            tracker = tracker.next
            slow = slow.next
            fast = fast.next.next
        tracker.next = slow.next
        slow.next = None
        return prev.next
        