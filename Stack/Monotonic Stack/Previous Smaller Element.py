class Solution:
    def prevSmaller(self, arr):
        st = []
        ans = []
        for x in arr:
            while st and st[-1] >= x:
                st.pop()
            ans.append(st[-1] if st else -1)
            st.append(x)
        return ans