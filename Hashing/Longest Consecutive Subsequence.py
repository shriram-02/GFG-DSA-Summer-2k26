class Solution:
    def longestConsecutive(self, arr):
        s = set(arr)
        ans = 0

        for x in s:
            if x - 1 not in s:
                curr = x
                cnt = 1
                while curr + 1 in s:
                    curr += 1
                    cnt += 1
                ans = max(ans, cnt)

        return ans