class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
            max_ones = max(max_ones,ones)
            if nums[i] == 0:
                ones = 0
        return max_ones