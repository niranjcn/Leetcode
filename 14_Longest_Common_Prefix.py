class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        res = ""
        while count < len(min(strs)):
            for i in range(1,len(strs)):
                if strs[0][count] != strs[i][count]:
                    return res
            res += strs[0][count]
            count += 1
        return res