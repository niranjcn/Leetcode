class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_vowels = 0
        curr_vowels = 0
        l = 0
        for r in range(len(s)):
            if (r-l+1) > k:
                if s[l] in vowels:
                    curr_vowels -= 1
                l += 1
            if s[r] in vowels:
                curr_vowels += 1
            max_vowels = max(max_vowels,curr_vowels)
        return max_vowels