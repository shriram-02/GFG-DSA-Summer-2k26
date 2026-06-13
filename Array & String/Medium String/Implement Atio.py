class Solution:
    def myAtoi(self, s):
        # code here
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        num = 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            num = num * 10 + digit
            i += 1
        return sign * num