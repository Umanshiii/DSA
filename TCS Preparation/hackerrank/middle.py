class node:
    def __init__(self,data):
        self.value=data
        self.next=None

def create(n, arr):
    head=node(arr[0])
    curr=head
    for i in range(1,n):
        curr.next=node(arr[i])
        curr=curr.next    
    return head

def middle(head):
    slow=head
    fast=head
    if len(arr)%2==0:
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
    else:
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

    return slow.value
        
n=6
arr=[1,3,5,56,2,4]
head=create(n,arr)
print(middle(head))
n=5
arr=[1,3,5,2,4]
head=create(n,arr)
print(middle(head))