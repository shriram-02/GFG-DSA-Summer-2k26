class Solution:
    def sortStrings(self, arr: list[str]) -> list[str]:
        # Python's built-in sort/sorted is stable
        return sorted(arr, key=len)