# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k==0:
            return head
        curr = head
        i = 1
        while curr.next:     
            curr = curr.next
            i+=1
        curr.next = head
        k = k%i
        tempNode = head
        for _ in range(1,i-k):
            tempNode = tempNode.next
        newHead = tempNode.next
        tempNode.next = None
        return newHead
        
        