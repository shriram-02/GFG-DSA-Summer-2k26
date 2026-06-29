class Solution:
    def catchThieves(self, arr, k):
        police = []
        thieves = []

        for i, ch in enumerate(arr):
            if ch == 'P':
                police.append(i)
            else:
                thieves.append(i)

        i = j = ans = 0

        while i < len(police) and j < len(thieves):
            if abs(police[i] - thieves[j]) <= k:
                ans += 1
                i += 1
                j += 1
            elif police[i] < thieves[j]:
                i += 1
            else:
                j += 1

        return ans