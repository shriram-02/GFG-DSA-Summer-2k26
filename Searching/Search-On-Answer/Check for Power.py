class Solution:
    def isPower(self, x, y):
        # Code here
        if x == 1:
            return y == 1
        val = 1
        while val < y:
            val *= x
        return val == y