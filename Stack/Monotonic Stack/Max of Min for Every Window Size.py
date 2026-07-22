class Solution:
    def maxOfMins(self, arr):
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        st = []

        for i in range(n):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            left[i] = st[-1] if st else -1
            st.append(i)

        st.clear()
        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            right[i] = st[-1] if st else n
            st.append(i)

        ans = [0] * (n + 1)
        for i in range(n):
            l = right[i] - left[i] - 1
            ans[l] = max(ans[l], arr[i])

        for i in range(n - 1, 0, -1):
            ans[i] = max(ans[i], ans[i + 1])

        return ans[1:]