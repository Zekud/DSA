# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        dummy = ListNode()
        point = dummy
        first = l1
        second = l2
        carry = 0 
        while first or second or carry:
            if first and second:
                if first.val + second.val + carry >= 10:
                    x = first.val + second.val + carry
                    y = str(x)
                    carry = int(y[0])
                    point.next = ListNode(int(y[1]))
                    point = point.next

                else:
                    x = first.val + second.val + carry
                    point.next = ListNode(x)
                    carry = 0
                    point = point.next
            elif first:
                x = first.val + carry
                if x >=10:
                    y = str(x)
                    carry = int(y[0])
                    point.next = ListNode(int(y[1]))
                    point = point.next
                else:
                    point.next = ListNode(x)
                    carry = 0
                    point = point.next
            elif second:
                x = second.val + carry
                if x >= 10:
                    y = str(x)
                    carry = int(y[0])
                    point.next = ListNode(int(y[1]))
                    point = point.next
                else:
                    point.next = ListNode(second.val + carry)
                    point = point.next
                    carry = 0
            elif carry:
                point.next = ListNode(carry)
                point = point.next
                carry = 0
            if first:
                first = first.next
            if second:
                second = second.next
        
    
        return dummy.next