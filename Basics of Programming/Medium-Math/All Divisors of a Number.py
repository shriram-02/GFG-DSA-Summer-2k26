class Solution:
    def getDivisors(self, n):
        # code here
        divisors = []
        i = 1

        while i * i <= n:
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
            i += 1

        divisors.sort()
        return divisors