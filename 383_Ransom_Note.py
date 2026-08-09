class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = {}
        for ch in ransomNote:
            magazine_count[ch] = 1 + magazine_count.get(ch,0)
        
        for ch in magazine:
            if ch in magazine_count:
                magazine_count[ch] -= 1
                if magazine_count[ch] == 0:
                    del magazine_count[ch]
        return len(magazine_count) == 0