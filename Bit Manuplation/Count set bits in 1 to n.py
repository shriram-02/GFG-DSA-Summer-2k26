class Solution:
    def countSetBits(self, n):
        # code here
        if n == 0:
            return 0

        x = 0
        while (1 << (x + 1)) <= n:
            x += 1

        bits_upto_2x = x * (1 << (x - 1)) if x else 0
        msb_bits = n - (1 << x) + 1
        rest = n - (1 << x)

        return bits_upto_2x + msb_bits + self.countSetBits(rest)