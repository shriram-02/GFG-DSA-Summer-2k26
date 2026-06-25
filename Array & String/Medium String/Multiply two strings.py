class Solution:
    def multiplyStrings(self, s1, s2):
        # code here
        sign = 1
        if s1[0] == '-':
            sign *= -1
            s1 = s1[1:]
        if s2[0] == '-':
            sign *= -1
            s2 = s2[1:]
        s1 = s1.lstrip('0')
        s2 = s2.lstrip('0')
        
        if not s1 or not s2:
            return "0"
        
        n , m = len(s1),len(s2)
        res = [0] * (n + m)
        
        for i in range(n - 1,-1,-1):
            for j in range(m - 1, -1 , -1):
                mul = (ord(s1[i]) - ord('0')) * (ord(s2[j]) - ord('0'))
                total = mul + res[i + j + 1]
                
                res[i + j + 1] = total % 10
                res[i + j] += total // 10
        result = ''.join(map(str,res)).lstrip('0')
        
        if sign == -1:
            result = '-' + result
        return result
                    
                
        
        