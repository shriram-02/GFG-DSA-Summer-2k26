class Solution:
    def reducePairs(self, arr):
        st = []
        for x in arr:
            if st and st[-1] == -x:
                st.pop()
            else:
                st.append(x)
        return st