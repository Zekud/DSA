# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # def getMiddle(head):
        #     fast,slow=head,head
        #     while fast.next and fast.next.next:
        #         slow=slow.next
        #         fast=fast.next.next
        #     return slow
        def mergeSort(left,right):
            dummy=ListNode()
            ptr=dummy
            while left and right:
                if left.val<right.val:
                    ptr.next=left
                    left=left.next
                    ptr=ptr.next
                else:
                    ptr.next=right
                    right=right.next
                    ptr=ptr.next
            ptr.next = left if left else right
            return dummy.next
        def merge(head):
            if not head or not head.next:
                return head
            fast,slow=head,head
            while fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
            
            right_head=slow.next
            slow.next=None
            left=merge(head)
            right=merge(right_head)
            return mergeSort(left,right)
       

        return merge(head)

            