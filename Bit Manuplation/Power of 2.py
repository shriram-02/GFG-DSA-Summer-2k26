class Solution:
    def isPowerOfTwo(self, n):
        # code here
        return n > 0 and (n & (n - 1)) == 0