class Solution:
    def reverseWords(self, s: str) -> str:
        temp = []
        res = ""
        j = 0
        for i in range(len(s)):
            if s[i] == " ":
                if s[j:i] != "":
                    temp.append(s[j:i]) 
                j = i+1
            if i == len(s)-1:
                if s[j:i+1] != "":
                    temp.append(s[j:i+1])
        
        for i in range(len(temp)-1,-1,-1):
            res += temp[i]
            if i != 0:
                res += " "
        return res