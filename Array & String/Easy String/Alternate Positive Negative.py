class Solution:
    def rearrange(self, arr):
        pos = [x for x in arr if x >= 0]
        neg = [x for x in arr if x < 0]

        i = j = 0
        ans = []

        while i < len(pos) and j < len(neg):
            ans.append(pos[i])
            ans.append(neg[j])
            i += 1
            j += 1

        while i < len(pos):
            ans.append(pos[i])
            i += 1

        while j < len(neg):
            ans.append(neg[j])
            j += 1

        return ans