class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        count = 0
        for ch in s:
            if ch == "(":
                count += 1
                if count > 1:
                    res += "("
            if ch == ")":
                count -= 1
                if count > 0:
                    res += ")"
        return res