class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right_sum = sum(nums)
        left_sum = 0
        res = []

        for num in nums:
            right_sum -= num
            res.append(abs(right_sum - left_sum))
            left_sum += num
        
        return res