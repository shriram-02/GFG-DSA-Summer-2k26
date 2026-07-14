class Solution:
    def intersectPoint(self, head1, head2):
        a, b = head1, head2

        while a != b:
            a = a.next if a else head2
            b = b.next if b else head1

        return a.data