class Solution:
    def rotate(self, n, d):
        # code here
        d %= 16
        left = ((n << d) | (n >> (16 - d))) & 0xFFFF
        right = ((n >> d) | (n << (16 - d))) & 0xFFFF
        return [left, right]