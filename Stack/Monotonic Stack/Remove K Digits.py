class Solution:
    def removeKdig(self, s, k):
        st = []
        for c in s:
            while k and st and st[-1] > c:
                st.pop()
                k -= 1
            st.append(c)
        while k:
            st.pop()
            k -= 1
        ans = "".join(st).lstrip('0')
        return ans if ans else "0"