class Solution:
    def calculateSpan(self, arr):
        st = []
        ans = []
        for i in range(len(arr)):
            while st and arr[st[-1]] <= arr[i]:
                st.pop()
            if not st:
                ans.append(i + 1)
            else:
                ans.append(i - st[-1])
            st.append(i)
        return ans