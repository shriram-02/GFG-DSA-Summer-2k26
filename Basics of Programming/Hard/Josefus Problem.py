class Solution:
    def josephus(self, n, k):
        # code here
        if n == 1:
            return 1
        return (self.josephus(n - 1, k) + k - 1) % n + 1