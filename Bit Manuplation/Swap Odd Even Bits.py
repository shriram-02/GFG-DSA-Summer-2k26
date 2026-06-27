class Solution:
    def swapBits(self, n):
        # code here
        even = n & 0xAAAAAAAA
        odd = n & 0x55555555
        return (even >> 1) | (odd << 1)