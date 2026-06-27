class Solution:
    def twoOddNum(self, arr):
        # code here
        xr = 0
        for x in arr:
            xr ^= x

        rsb = xr & -xr
        a = b = 0

        for x in arr:
            if x & rsb:
                a ^= x
            else:
                b ^= x

        return [max(a, b), min(a, b)]