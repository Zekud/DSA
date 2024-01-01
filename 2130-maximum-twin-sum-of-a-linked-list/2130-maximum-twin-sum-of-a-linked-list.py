# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = ListNode() #dummy node
        prevList = []
        twinSum = 0
        slow, fast = head,head
        while fast and fast.next:
            prev.next = slow
            prev = prev.next
            prevList.append(prev.val)
            slow = slow.next
            fast = fast.next.next
        i=len(prevList)-1
        while slow:
            twinSum = max(twinSum, slow.val + prevList[i])
            slow = slow.next
            i-=1
        return twinSum
        
        