class Solution:
    def isPalindrome(self, n):
        # code here
        return str(n) == str(n)[::-1]