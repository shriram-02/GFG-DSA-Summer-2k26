class Solution:
    def nextPalindrome(self, num):
        # code here
        n = len(num)
        ans = num[:]
        
        for i in range(n // 2):
            ans[n - 1 - i] = ans[i]
        if ans > num:
            return ans
        carry = 1
        mid = (n - 1) // 2
        
        while mid  >= 0 and carry:
            ans[mid] += carry
            carry = ans[mid] // 10
            ans[mid] %= 10
            mid -= 1
        if carry:
            return [1] + [0] * (n - 1) + [1]
        for i in range(n // 2):
            ans[n - 1 - i] = ans[i]
        return ans 