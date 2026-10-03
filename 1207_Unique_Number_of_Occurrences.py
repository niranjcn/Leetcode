class Solution:
    def uniqueOccurrences(self, nums: list[int]) -> bool:
        freq = {}
        res = set()
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        for num in freq.values():
            if num in res:
                return False
            res.add(num)
        return True