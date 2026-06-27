class Solution:
    def checkKthBit(self, n, k):
        # code here
        return (n & (1 << k)) != 0