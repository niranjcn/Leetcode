class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[True]*len(s) for _ in range(len(s))]
        
        start, max_length = 0, 1

        for i in range(len(s)-2,-1,-1):
            for j in range(i+1,len(s)):
                dp[i][j] = False
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                
                if dp[i][j] and max_length < j - i + 1:
                    start = i
                    max_length = j - i + 1
        
        return s[start:start+max_length]