class Solution:
    def graycode(self, n):
        # code here
        ans = []
        for i in range(1 << n):
            g = i ^ (i >> 1)
            ans.append(format(g, f'0{n}b'))
        return ans