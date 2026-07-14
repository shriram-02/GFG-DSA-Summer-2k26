class Solution:
    def isPalindrome(self, head):
        vals = []
        while head:
            vals.append(head.data)
            head = head.next
        return vals == vals[::-1]