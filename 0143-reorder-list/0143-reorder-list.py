# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_half = self.reverse(slow.next) #getting the head of the second half after                                                      reversing
        
        slow.next = None                        #setting firstHalf to end
        while second_half:
            first_half_nextNode = head.next
            second_half_nextNode = second_half.next
            head.next = second_half
            second_half.next = first_half_nextNode
            head = first_half_nextNode
            second_half = second_half_nextNode
        
        
    def reverse(self, newHead):
        curr = newHead
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev
            
        