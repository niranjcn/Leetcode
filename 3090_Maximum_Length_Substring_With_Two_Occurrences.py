class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = {}
        res = 0
        l = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r],0)
            while freq[s[r]] > 2:
                freq[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res