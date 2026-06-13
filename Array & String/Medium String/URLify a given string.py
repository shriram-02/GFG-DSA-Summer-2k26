class Solution:
    def URLify(self, s): 
        # code here
        ans = ""
        for ch in s:
            if ch == ' ':
                ans += "%20"
            else:
                ans += ch
        return ans 
