class Solution:
    def gcd(self, a, b):
        # code here
        while b:
            a , b = b, a % b
        return a