class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l,res = 0,0
        count = {}
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            
            while len(count) == 3:
                res += len(s) - r
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
        return res