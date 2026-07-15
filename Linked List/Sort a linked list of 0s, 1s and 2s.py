class Solution:
    def segregate(self, head):
        count = [0, 0, 0]
        temp = head

        while temp:
            count[temp.data] += 1
            temp = temp.next

        temp = head
        i = 0

        while temp:
            while count[i] == 0:
                i += 1
            temp.data = i
            count[i] -= 1
            temp = temp.next

        return head