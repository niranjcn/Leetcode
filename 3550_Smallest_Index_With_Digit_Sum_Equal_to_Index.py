class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            digit = nums[i]
            res = 0
            while digit > 0:
                res += digit % 10
                digit //= 10
            if res == i:
                return i
        return -1