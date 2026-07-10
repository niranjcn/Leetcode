from typing import List 
class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        anagram = {} 
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagram:
                anagram.get(sorted_word).append(word)
            else:
                anagram[sorted_word] = [word] 
        return [word for word in anagram.values()]