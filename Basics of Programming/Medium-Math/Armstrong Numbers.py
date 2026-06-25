class Solution:
    def armstrongNumber(self, n):
        # code here
        temp = n
        s = 0

        while temp > 0:
            digit = temp % 10
            s += digit ** 3
            temp //= 10

        return s == n