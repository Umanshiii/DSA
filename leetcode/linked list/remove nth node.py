# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        l=0
        if head is None:
            return None
        while curr!=None:
            curr=curr.next
            l+=1
        if l == n:
            return head.next
        curr=head
        for i in range(1,l-n):
            curr=curr.next
        curr.next=curr.next.next
        return head