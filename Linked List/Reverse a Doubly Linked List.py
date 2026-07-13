class Solution:
    def reverse(self, head):
        curr = head
        new_head = None

        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            new_head = curr
            curr = curr.prev

        return new_head