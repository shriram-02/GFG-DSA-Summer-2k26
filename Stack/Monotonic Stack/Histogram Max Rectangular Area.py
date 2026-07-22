class Solution:
    def getMaxArea(self, arr):
        st = []
        ans = 0
        arr.append(0)
        for i, h in enumerate(arr):
            while st and arr[st[-1]] > h:
                height = arr[st.pop()]
                width = i if not st else i - st[-1] - 1
                ans = max(ans, height * width)
            st.append(i)
        arr.pop()
        return ans