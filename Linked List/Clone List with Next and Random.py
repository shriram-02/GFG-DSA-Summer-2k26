class Solution:
    def cloneLinkedList(self, head):
        if not head:
            return None

        curr = head
        while curr:
            new = Node(curr.data)
            new.next = curr.next
            curr.next = new
            curr = new.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        copy_head = head.next
        copy = copy_head

        while curr:
            curr.next = copy.next
            curr = curr.next
            if curr:
                copy.next = curr.next
                copy = copy.next

        return copy_head