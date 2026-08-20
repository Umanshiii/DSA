# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        curr1=l1
        curr2=l2
        head = ListNode(0)
        curr=head
        carry = 0
        while curr1 or curr2 or carry:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            total=val1+val2 + carry

            carry = total // 10
            digit = total % 10
                
            new=ListNode(digit)
            curr.next=new
            curr=new
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
            
        return head.next