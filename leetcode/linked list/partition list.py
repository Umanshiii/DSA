# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(0)
        large = ListNode(0)
        ends = small
        endl = large

        curr = head

        while curr:
            node = curr.next
            curr.next = None 
            if curr.val < x:
                ends.next = curr
                ends = ends.next
            else:
                endl.next = curr
                endl = endl.next

            curr = node

        ends.next = large.next

        return small.next
