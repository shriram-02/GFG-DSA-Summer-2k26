class Solution:
    def isPalinSent(self, s):
        t = "".join(ch.lower() for ch in s if ch.isalnum())
        return t == t[::-1]