class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        def backtrack(cur,open_used,close_used):
            if len(cur) == 2 * n:
                stack.append(cur)
                return
            if open_used < n:
                backtrack(cur + "(", open_used + 1, close_used)
            if close_used < open_used:
                backtrack(cur + ")",open_used,close_used+1)
        backtrack("",0,0)
        return stack