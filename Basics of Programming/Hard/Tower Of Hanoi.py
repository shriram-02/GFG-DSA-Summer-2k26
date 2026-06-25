class Solution:
    def towerOfHanoi(self, n, fromm, to, aux):
        # code here
        return (1 << n) - 1