class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_len = 1
        for num in seen:
            if num - 1 not in seen:
                length = 1
                while num + length in seen:
                    length += 1
                max_len = max(max_len,length)
            
            
        return max_len if len(nums) > 0 else 0