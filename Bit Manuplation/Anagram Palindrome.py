class Solution:
    def canFormPalindrome(self, s):
        # code here
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        odd = 0
        for x in freq:
            if x % 2:
                odd += 1

        return odd <= 1