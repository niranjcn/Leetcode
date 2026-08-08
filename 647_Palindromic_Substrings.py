class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[True] * len(s) for _ in range(len(s))]
        count = len(s)
        for i in range(len(s)-2,-1,-1):
            for j in range(i+1,len(s)):
                dp[i][j] = False
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                    if dp[i][j] == True:
                        count += 1
        return count