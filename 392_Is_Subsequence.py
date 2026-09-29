class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0

        for char in t:
            if left < len(s) and s[left] == char:
                left += 1

        return left == len(s)