class Solution:
    def lengthOfLoop(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                cnt = 1
                temp = slow.next
                while temp != slow:
                    cnt += 1
                    temp = temp.next
                return cnt
        return 0