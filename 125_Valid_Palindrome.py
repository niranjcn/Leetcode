class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = "".join(ch.lower() for ch in s if ch.isalnum())
        for i in range(len(strs)):
            if strs[i] != strs[(len(strs)-1-i)]:
                return False
        return True