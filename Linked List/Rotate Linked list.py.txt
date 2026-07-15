'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def rotate(self, head, k):
        # code here
        if not head or not head.next:
            return head
        curr=head
        n=1
        while curr.next:
            curr=curr.next
            n+=1
        k=k%n   
        if k==0:
            return head
        curr.next=head
        steps=k
        new_tail=head
        while steps > 1:
            new_tail=new_tail.next
            steps-=1
        new_head=new_tail.next
        new_tail.next=None
        return new_head