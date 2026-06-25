class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        # code here
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)