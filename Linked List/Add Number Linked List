'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def addTwoLists(self, head1, head2):
        # code here
        def reverse(head):
            prev=None
            curr=head
            while curr:
                next_node=curr.next
                curr.next=prev
                prev=curr
                curr=next_node
            return prev
        while head1 and head1.data==0 and head1.next:
            head1=head1.next
        while head2 and head2.data==0 and head2.next:
            head2=head2.next
        l1=reverse(head1)
        l2=reverse(head2)
        
        carry=0
        dummy=Node(0)
        temp=dummy
        
        while l1 or l2 or carry:
            x=l1.data if l1 else 0
            y=l2.data if l2 else 0
            
            total=x+y+carry
            carry=total//10
                
            temp.next=Node(total%10)
            temp=temp.next
            
            if l1: l1=l1.next
            if l2:l2=l2.next
        return reverse(dummy.next)
        while rea and res.data==0 and res.next:
            res=res.next
        return res