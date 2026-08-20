class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head

        cur1 = list1
        cur2 = list2

        while cur1 is not None and cur2 is not None:
            if cur1.val < cur2.val:
                curr.next = cur1
                cur1 = cur1.next
            else:
                curr.next = cur2
                cur2 = cur2.next

            curr = curr.next


        if cur1 is not None:
            curr.next = cur1
        else:
            curr.next = cur2

        return head.next


