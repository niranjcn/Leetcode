class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin, currMax = 1, 1

        for num in nums:
            tmp = currMax * num
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(num * currMin, tmp, num)
            res = max(res,currMax)
        return res