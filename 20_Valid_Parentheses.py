class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"}":"{",")":"(","]":"["}
        for bracket in s:
            if bracket in brackets.values():
                stack.append(bracket)
            else:
                if not stack or stack[-1] != brackets[bracket]:
                    return False
                stack.pop()
        return  len(stack) == 0