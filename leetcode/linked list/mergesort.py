# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        fast,slow=head.next,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        mid = slow
        half = mid.next
        mid.next = None
        left = self.sortList(head) 
        right = self.sortList(half)
        return self.merge(left, right)
    
    def merge(self,left,right):
        dummy=ListNode(0)
        curr=dummy
        while left and right:
            if left.val<=right.val:
                curr.next=left
                left=left.next
            else:
                curr.next=right
                right=right.next
            curr=curr.next

        if left and not right:
            curr.next=left

        if right and not left:
            curr.next=right

        return dummy.next

